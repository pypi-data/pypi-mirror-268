# from dataclasses import dataclass, field
from typing import List

from pydantic import BaseModel, Extra, field


class Domain(BaseModel):
    domainname: str

    id: str = None
    organisation: str = None
    ownerfirstname: str = None
    ownerlastname: str = None
    ownercompanyname: str = None
    ownerstreetaddress: str = None
    ownercity: str = None
    ownerstate: str = None
    ownerpostalcode: str = None
    ownercountry: str = None
    ownerphone: str = None
    ownerfax: str = None
    owneremail: str = None
    adminlastname: str = None
    admincompanyname: str = None
    adminstreetaddress: str = None
    admincity: str = None
    adminstate: str = None
    adminpostalcode: str = None
    admincountry: str = None
    adminphone: str = None
    adminfax: str = None
    adminemail: str = None
    billfirstname: str = None
    billlastname: str = None
    billcompanyname: str = None
    billstreetaddress: str = None
    billcity: str = None
    billstate: str = None
    billpostalcode: str = None
    billcountry: str = None
    billphone: str = None
    billfax: str = None
    billemail: str = None
    techfirstname: str = None
    techlastname: str = None
    techcompanyname: str = None
    techstreetaddress: str = None
    techcity: str = None
    techstate: str = None
    techcountry: str = None
    techpostalcode: str = None
    techphone: str = None
    techfax: str = None
    techemail: str = None
    auto_renew: str = None
    reg_opt_out: str = None
    username: str = None
    editzone: str = None
    expires: str = None
    deleteonexpiry: str = None
    companyregno: str = None
    client_delete_prohibited_lock: str = None
    client_update_prohibited_lock: str = None
    client_transfer_prohibited_lock: str = None
    registeredhere: str = None
    nameservers: List[str] = field(default_factory=list)

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

    def is_same(self, right: "Domain") -> bool:
        """
        This method check the identity (e.g. same id if defined, or same name/name+value)
        """
        if not isinstance(right, Domain):
            return NotImplemented
        return self.domainname == self.right


class Domains:
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

    def get(self, domain: str, timeout=None):
        url = f"/domain/{domain}"
        res = self.client.get(
            url,
            timeout=timeout,
        )
        return [Domain(**d) for d in res]

    # def get(self, domain: str, record_id, timeout=None):
    #     res = self.client.list(
    #         domain,
    #         timeout=timeout,
    #     )
    #     return next((r for r in res if r.id == record_id), None)
