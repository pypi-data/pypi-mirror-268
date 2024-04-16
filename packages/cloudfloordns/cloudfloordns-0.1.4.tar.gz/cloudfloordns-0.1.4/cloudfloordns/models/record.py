# from dataclasses import dataclass, field
from typing import Literal

from pydantic import BaseModel, Extra

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
