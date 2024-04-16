import ipih

from pih.consts import CONST
from pih.consts.hosts import Hosts
from pih.collections.service import ServiceDescription

NAME: str = "PolibasePersonReviewAutomation"

HOST = Hosts.BACKUP_WORKER

VERSION: str = "0.15"

SD: ServiceDescription = ServiceDescription(
    name=NAME,
    description="Polibase person review automation service",
    host=HOST.NAME,
    use_standalone=True,
    version=VERSION,
    standalone_name="plb_rvw_auto",
    run_from_system_account=True,
    python_executable_path=CONST.UNKNOWN,
)
