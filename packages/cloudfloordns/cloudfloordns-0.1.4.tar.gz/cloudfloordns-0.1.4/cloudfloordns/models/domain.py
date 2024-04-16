# from dataclasses import dataclass, field
from typing import List, Optional

from pydantic import BaseModel, StringConstraints
from typing_extensions import Annotated

DEFAULT_PRIMARY_NS = "ns1.g02.cfdns.net"


class Domain(BaseModel):
    domainname: Annotated[str, StringConstraints(strip_whitespace=True)]

    id: str = None
    zone: str = None
    registered: int = None
    secondary: int = None
    primary: int = None
    group_ids: Optional[List[str]] = None

    class Config:
        populate_by_name = True
        extra = "allow"

    # def __eq__(self, __value: Record) -> bool:
    #     if not isinstance(__value, Record):
    #         return NotImplemented
    #     fields1 = self.model_dump(exclude_unset=True)
    #     fields2 = __value.model_dump(exclude_unset=True)
    #     try:
    #         return all(fields2[k] == v for k, v in fields1.items())
    #     except Exception:
    #         return False

    def __hash__(self):
        return hash(self.domainname)

    def __eq__(self, op):
        return self.is_same(op)

    def is_same(self, right: "Domain") -> bool:
        """
        This method check the identity
        """
        if not isinstance(right, (Domain, str)):
            return NotImplemented
        if isinstance(right, Domain):
            right = right.domainname
        return self.domainname == right
