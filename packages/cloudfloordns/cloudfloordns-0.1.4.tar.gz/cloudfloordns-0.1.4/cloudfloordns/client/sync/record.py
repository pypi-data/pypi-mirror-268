# from dataclasses import dataclass, field
from typing import List

from cloudfloordns.models import Record


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
