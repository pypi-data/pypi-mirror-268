# from dataclasses import dataclass, field
from typing import List

from pydantic import BaseModel, Field, StringConstraints
from typing_extensions import Annotated

DEFAULT_PRIMARY_NS = "ns1.g02.cfdns.net"


class Group(BaseModel):
    id: str = None
    name: Annotated[str, StringConstraints(strip_whitespace=True)]
    description: str = None
    dnsservers: List[str] = Field(default_factory=list)

    class Config:
        populate_by_name = True
        extra = "allow"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, op):
        if isinstance(op, Group):
            op = Group.name
        return self.name == op


class Groups:
    def __init__(self, client) -> None:
        self.client = client

    # def create(self, domain: str, record: Record, timeout=None):
    #     url = f"/dns/zone/{domain}/record"
    #     return self.client.post(
    #         url,
    #         data=record.model_dump(),
    #         timeout=timeout,
    #     )

    # def update(self, domain: str, record_id: str, record: Record, timeout=None):
    #     url = f"/dns/zone/{domain}/record/{record_id}"
    #     return self.client.patch(
    #         url,
    #         data=record.model_dump(exclude_unset=True),
    #         timeout=timeout,
    #     )

    # def delete(self, domain: str, record_id: str, timeout=None):
    #     url = f"/dns/zone/{domain}/record/{record_id}"
    #     return self.client.delete(
    #         url,
    #         timeout=timeout,
    #     )

    def list(self, timeout=None):
        url = "/manage/groups"
        res = self.client.get(
            url,
            timeout=timeout,
        )
        return [Group(**d) for d in res]

    def get(self, group_id, timeout=None):
        res = self.list(
            timeout=timeout,
        )
        return next((r for r in res if r.id == group_id), None)

    def get_by_name(self, name, timeout=None):
        res = self.list(
            timeout=timeout,
        )
        return next((r for r in res if r.name == name), None)
