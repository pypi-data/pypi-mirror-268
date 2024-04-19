import ipih

from pih.consts.hosts import Hosts
from pih.collections.service import ServiceDescription

NAME: str = "AnswerAutomation"

HOST = Hosts.BACKUP_WORKER

VERSION: str = "0.17"

SD: ServiceDescription = ServiceDescription(
    name=NAME,
    description="Answer automation service",
    host=HOST.NAME,
    use_standalone=True,
    version=VERSION,
    standalone_name="answ_auto",
)
