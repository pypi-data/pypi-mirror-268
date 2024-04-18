import ipih

from pih.consts.hosts import Hosts
from pih.collections.service import ServiceDescription

NAME: str = "IOTDevices"

HOST = Hosts.WS255

MODULES: tuple[str, ...] = ("tinytuya",)

VERSION: str = "0.12"

API_REGION: str = "eu"
API_KEY: str = "ss88c577cc4nex5sqf8u"
API_SECRET: str = "b3eb6c41acf2465cb48bb366ba6c0fd2"

SD: ServiceDescription = ServiceDescription(
    name=NAME,
    description="IOT Devices service",
    host=HOST.NAME,
    use_standalone=True,
    host_changeable=True,
    standalone_name="iot",
    version=VERSION,
    packages=MODULES,
)
