# from dataclasses import dataclass, field
from cloudfloordns.models import Domain

from .pool import POOL

DEFAULT_PRIMARY_NS = "ns1.g02.cfdns.net"


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

    def update(self, domain: "Domain", soa=None, timeout=None):
        url = "/dns/zone"
        data = domain.model_dump(exclude_unset=True)
        if not soa:
            soa = self.soa(domain)

        data = domain.model_dump(exclude_unset=True)
        soa_data = {
            "master": soa["ns"],  # NS: primary name server
            "retry": soa[
                "retry"
            ],  # Retry: How often secondaries attempt to fetch the zone if the first refresh fails
            "refresh": soa[
                "refresh"
            ],  # Refresh:  How often secondaries should check if changes are made to the zone
            "expire": soa[
                "expire"
            ],  # Expire: Secondaries will discard the zone if no refresh could be made within this interval.
            "min": soa[
                "minimum"
            ],  #  Min TTL: default TTL for new records. Also determines how long negative records are cached (record not found)
            "mbox": soa[
                "mbox"
            ],  # RP: Responsible person (email address with period instead of '@')
            "ttl": soa[
                "ttl"
            ],  # SOA TTL: Number of seconds this zone may be cached before the source must be consulted again.
        }
        request_data = {**soa_data, **data}
        return self.client.patch(
            url,
            data=request_data,
            timeout=timeout,
        )

    def disable(self, domain: str, timeout=None):
        url = f"/dns/zone/{domain}"
        return self.client.delete(
            url,
            timeout=timeout,
        )

    def delete(self, domain: str, timeout=None):
        url = f"/domain/{domain}/delete_domain"
        return self.client.delete(
            url,
            timeout=timeout,
        )

    def _list_all(self, timeout=None):
        url = "/dns"
        res = self.client.get(
            url,
            timeout=timeout,
        )
        return [Domain(**d) for d in res]

    def _list_enabled(self, timeout=None):
        url = "/dns/zone"
        res = self.client.get(
            url,
            timeout=timeout,
        )
        return [Domain(**d) for d in res]

    def enable(
        self,
        domain,
        master=DEFAULT_PRIMARY_NS,
        # master="dns0.mtgsy.co.uk.",
        retry=1200,
        refresh=3600,
        expire=1209600,
        min=3600,
        responsible="hostmaster",
        ttl=86400,
        timeout=None,
    ):
        if isinstance(domain, Domain):
            domain = domain.domainname
        url = f"/dns/zone/{domain}/enable"
        # This will create the SOA record
        # The default values can be found on an active domain
        return self.client.patch(
            url,
            data={
                "domainname": domain,
                "master": master,  # NS: primary name server
                "retry": retry,  # Retry: How often secondaries attempt to fetch the zone if the first refresh fails
                "refresh": refresh,  # Refresh:  How often secondaries should check if changes are made to the zone
                "expire": expire,  # Expire: Secondaries will discard the zone if no refresh could be made within this interval.
                "min": min,  #  Min TTL: default TTL for new records. Also determines how long negative records are cached (record not found)
                "mbox": responsible,  # RP: Responsible person (email address with period instead of '@')
                "ttl": ttl,  # SOA TTL: Number of seconds this zone may be cached before the source must be consulted again.
            },
            timeout=timeout,
        )

    def enable_all(
        self,
        master=DEFAULT_PRIMARY_NS,
        # master="dns0.mtgsy.co.uk.",
        retry=1200,
        refresh=3600,
        expire=1209600,
        min=3600,
        responsible="hostmaster",
        ttl=86400,
        timeout=None,
    ):
        domains = self.list(zone_enabled=False)

        def worker(domain):
            try:
                return self.enable(
                    domain,
                    master=master,
                    retry=retry,
                    refresh=refresh,
                    expire=expire,
                    min=min,
                    responsible=responsible,
                    ttl=ttl,
                    timeout=timeout,
                )
            except Exception as e:
                return str(e)

        return POOL.map(worker, domains)

    def list(self, zone_enabled=None, timeout=None):
        if zone_enabled is None:
            return self._list_all(timeout=timeout)
        if zone_enabled:
            return self._list_enabled(timeout=timeout)
        enabled = {d.domainname for d in self._list_enabled(timeout=timeout)}
        all_domains = self._list_all(timeout=timeout)
        return [d for d in all_domains if d.domainname not in enabled]

    def get(self, domain_id, zone_enabled=None, timeout=None):
        res = self.list(
            zone_enabled=zone_enabled,
            timeout=timeout,
        )
        return next((r for r in res if r.id == domain_id), None)

    def get_by_name(self, domainname, zone_enabled=None, timeout=None):
        res = self.list(
            zone_enabled=zone_enabled,
            timeout=timeout,
        )
        return next((r for r in res if r.domainname == domainname), None)

    def soa(self, domain, timeout=None):
        if isinstance(domain, Domain):
            domain = domain.domainname
        url = f"/dns/zone/{domain}/soa"
        return self.client.get(
            url,
            timeout=timeout,
        )

    def update_soa(
        self,
        domain,
        master=None,
        serial=None,
        retry=None,
        refresh=None,
        expire=None,
        min=None,
        responsible=None,
        ttl=None,
        xfer=None,
        timeout=None,
    ):
        if isinstance(domain, Domain):
            domain = domain.domainname
        url = f"/dns/zone/{domain}/soa"
        data = {
            "ns": master,  # NS: primary name server
            "retry": retry,  # Retry: How often secondaries attempt to fetch the zone if the first refresh fails
            "refresh": refresh,  # Refresh:  How often secondaries should check if changes are made to the zone
            "expire": expire,  # Expire: Secondaries will discard the zone if no refresh could be made within this interval.
            "minimum": min,  #  Min TTL: default TTL for new records. Also determines how long negative records are cached (record not found)
            "mbox": responsible,  # RP: Responsible person (email address with period instead of '@')
            "ttl": ttl,  # SOA TTL: Number of seconds this zone may be cached before the source must be consulted again.
            "serial": serial,
            "xfer": xfer,
        }
        data = {k: v for k, v in data.items() if v is not None}
        return self.client.patch(
            url,
            data=data,
            timeout=timeout,
        )
