import ipih
from pih.consts.hosts import Hosts
from pih.collections.service import ServiceDescription

NAME: str = "Mail"
SECTION: str = "MailboxInfo"

HOST = Hosts.WS255

# 0.1 - Persistance caching for email address deliverability checking status and  recall for email deliverability checking if status == UNKNOWN
# 0.12 - using new method for checking mail deliverity
VERSION: str = "0.16"

TIMEOUT: int = 10
TRY_AGAIN_COUNT: int = 5
TRY_AGAIN_SLEEP_TIME: int = 1
PACKAGES: tuple[str, ...] = (
    "imap_tools",
    "dnspython",
)

SD: ServiceDescription = ServiceDescription(
    name=NAME,
    description="Mail service",
    host=HOST.NAME,
    commands=(
        "check_email_accessibility",
        "send_email",
        "get_email_information",
        "check_email_external",
    ),
    standalone_name="mail",
    use_standalone=True,
    version=VERSION,
    packages=PACKAGES,
)

EMAIL_STATUS_FIELD: str = "deliverability"
SECTION: str = "email_info"
SECTION_DELIVERITY: str = "email_" + EMAIL_STATUS_FIELD


class EMAIL_DELIVERABILITY_STATUS:

    UNKNOWN = "UNKNOWN"
    YES = "DELIVERABLE"
    NO = "UNDELIVERABLE"
