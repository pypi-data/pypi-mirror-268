import ipih

from pih.consts.hosts import Hosts
from pih.collections.service import ServiceDescription

NAME: str = "BonusProgram"

HOST = Hosts.BACKUP_WORKER

VERSION: str = "0.11"

SD: ServiceDescription = ServiceDescription(
    name=NAME,
    description="Bonus Program service",
    host=HOST.NAME,
    use_standalone=True,
    version=VERSION,
    standalone_name="bonus",
)
