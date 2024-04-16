# from dataclasses import dataclass, field
from typing import Iterable, List, Literal, Optional

from pydantic import BaseModel, Extra

from .utils import groupby

TYPES_VALUES = Literal[
    "A",
    "AAAA",
    "ALIAS",
    "CNAME",
    "HINFO",
    "MX",
    "NS",
    "PTR",
    "RP",
    "SRV",
    "CAA",
    "TXT",
    "REDIRECT://",
    # For comparison, the following are valid on Cloudflare
    # "SOA",
    # "DS",
    # "DNSKEY",
    # "LOC",
    # "NAPTR",
    # "SSHFP",
    # "SVCB",
    # "TSLA",
    # "URI",
    # "SPF",
]

FULL_COMPARISON = {
    "A",
    "AAAA",
    "ALIAS",
    "CNAME",
}

UNIQUE_BY_NAME = {"HINFO", "MX", "NS", "PTR", "RP", "SRV", "CAA", "TXT", "REDIRECT://"}


class Record(BaseModel):
    name: str
    type: str
    data: str
    id: str = None
    zone: str = None
    aux: str = "0"
    ttl: int = 3600
    active: Literal["Y", "N"] = "Y"
    # isfwd: str = "0"
    # cc: str = None
    # lbType: str = "0"

    class Config:
        populate_by_name = True
        extra = Extra.allow

    # def __eq__(self, __value: Record) -> bool:
    #     if not isinstance(__value, Record):
    #         return NotImplemented
    #     fields1 = self.model_dump(exclude_unset=True)
    #     fields2 = __value.model_dump(exclude_unset=True)
    #     try:
    #         return all(fields2[k] == v for k, v in fields1.items())
    #     except Exception:
    #         return False

    @property
    def identifier(self) -> bool:
        """
        This method returns an identifer for the record that does not depend on its remote id
        """
        identifier = f"{self.name}/{self.type}"
        if self.type in FULL_COMPARISON:
            identifier = f"{identifier}/{self.data}"
        return identifier

    def __hash__(self):
        return hash(self.identifier)

    def is_same(self, right: "Record") -> bool:
        """
        This method check the identity (e.g. same id if defined, or same name/name+value)
        """
        if not isinstance(right, Record):
            return NotImplemented
        if self.id and right.id:
            return self.id == right.id
        if (self.name, self.type) != (right.name, right.type):
            return False
        if self.type in FULL_COMPARISON:
            return self.data == right.data
        return True

    @property
    def contains_spf_definition(self) -> bool:
        # RFC states that we only have one spf record on the APEX
        # But we may defined other records with spf definition to be included elsewhere.
        return all((self.type == "TXT", "v=spf" in self.data.lower()))

    @property
    def is_spf(self) -> bool:
        # RFC:
        # https://www.rfc-editor.org/rfc/rfc6242#section-4.1
        # https://datatracker.ietf.org/doc/html/rfc7208#section-4.5
        # NOTE: There should be only 1 apex spf record,
        # but we can create other spf record (e.g. spf1.mydomain.com) and include it in the apex
        # (alternatively, we can define spf records with CNAME or even NS records)
        return all((not self.name, self.contains_spf_definition))

    @property
    def is_dkim(self) -> bool:
        return all(
            (
                "._domainkey" in self.name,
                self.type == "TXT",
                "v=dkim" in self.data.lower(),
            )
        )

    @property
    def is_dmarc(self) -> bool:
        return all(
            ("_dmarc" in self.name, self.type == "TXT", "v=dmarc" in self.data.lower())
        )


def default_sort_key(record: Record):
    return record.name, record.type, record.data


class RecordSet:
    def __init__(self, records: Optional[Iterable[Record]] = None):
        if records is None:
            records = []
        self._records = list(records)

    def __str__(self):
        return str(self._records)

    def __repr__(self):
        return f"RecordSet{self._records}"

    def __len__(self):
        return len(self._records)

    def __contains__(self, record: Record):
        return record in self._records

    def __iter__(self):
        return iter(self._records)

    def deduplicate(self):
        self._records = list(set(self._records))
        return self

    def sort(self, key=None, reverse=False):
        if key is None:
            key = default_sort_key
        self._records.sort(key=key, reverse=reverse)
        return self

    def clear(self):
        return self._records.clear()

    def append(self, record: Record):
        self._records.append(record)
        return self

    def extend(self, records: Iterable[Record]):
        self._records.extend(records)
        return self

    def copy(self):
        return RecordSet(self._records.copy())

    def filtered(self, predicat):
        return RecordSet(filter(predicat, self))

    @property
    def has_duplicates(self):
        return len(set(self._records)) != len(self._records)

    @property
    def duplicates(self):
        return {
            k: records
            for k, records in groupby(self._records, lambda r: r.identifier)
            if len(records) > 1
        }

    @property
    def spf_records(self):
        return [r for r in self._records if r.is_spf]

    @property
    def dkim_records(self):
        return [r for r in self._records if r.is_dkim]

    @property
    def dmarc_records(self):
        return [r for r in self._records if r.is_dmarc]

    @property
    def mx_records(self):
        return [r for r in self._records if r.type == "MX"]

    @property
    def hardening(self):
        return all(
            (
                len(self.spf_records) == 1,
                self.dkim_records,
                len(self.dmarc_records) == 1,
                self.mx_records,
            )
        )


# @make_methods_async
class Records:
    def __init__(self, client) -> None:
        self.client = client

    def create(self, domain: str, record: Record, timeout=None):
        url = f"/dns/zone/{domain}/record"
        return self.client.post(
            url,
            data=record.model_dump(),
            timeout=timeout,
        )

    def update(self, domain: str, record_id: str, record: Record, timeout=None):
        url = f"/dns/zone/{domain}/record/{record_id}"
        return self.client.patch(
            url,
            data=record.model_dump(exclude_unset=True),
            timeout=timeout,
        )

    def delete(self, domain: str, record_id: str, timeout=None):
        url = f"/dns/zone/{domain}/record/{record_id}"
        return self.client.delete(
            url,
            timeout=timeout,
        )

    def list(self, domain: str, timeout=None) -> List[Record]:
        url = f"/dns/zone/{domain}/record"
        try:
            res = self.client.get(
                url,
                timeout=timeout,
            )
            return [Record(**d) for d in res]
        except Exception as e:
            if "No record available for this domain" in str(e):
                return []
            raise

    def get(self, domain: str, record_id, timeout=None):
        res = self.client.list(
            domain,
            timeout=timeout,
        )
        return next((r for r in res if r.id == record_id), None)
