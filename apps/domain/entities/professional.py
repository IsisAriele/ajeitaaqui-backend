from dataclasses import dataclass

from apps.domain.entities.client import Client


@dataclass
class Professional(Client):
    pass
