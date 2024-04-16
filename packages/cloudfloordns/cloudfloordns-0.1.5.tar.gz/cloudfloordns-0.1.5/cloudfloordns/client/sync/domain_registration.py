from cloudfloordns.models import DomainRegistration


class DomainRegistrations:
    def __init__(self, client) -> None:
        self.client = client

    def get(self, domain, timeout=None) -> DomainRegistration:
        url = f"/domain/{domain}"
        res = self.client.get(
            url,
            timeout=timeout,
        )
        return DomainRegistration.model_validate(res)
