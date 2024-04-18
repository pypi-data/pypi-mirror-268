import ipih

from pih import A
from IOTDevicesService.const import *


SC = A.CT_SC


def start(as_standalone: bool = False) -> None:

    from tinytuya import Cloud
    from pih.consts.iot import IOT

    if A.U.for_service(SD):

        from typing import Any
        from pih.tools import ParameterList
        class DH:
            cloud: Cloud | None = None
        
        def service_starts_handler() -> None:
            DH.cloud = Cloud(
                        apiRegion=API_REGION,
                        apiKey=API_KEY,
                        apiSecret=API_SECRET,
                    )

        def service_call_handler(sc: SC, pl: ParameterList) -> Any:
            if sc == SC.serve_command:
                command: IOT.Commands = pl.next(IOT.Commands)
                if command == IOT.Commands.device_list:
                    return A.R.pack(None, DH.cloud.getdevices())
                if command == IOT.Commands.device_status_properties:
                    return A.R.pack(None, DH.cloud.getproperties(pl.next()))
                if command == IOT.Commands.device_status:
                    return A.R.pack(None, DH.cloud.getstatus(pl.next()))
            return None

        A.SRV_A.serve(SD, service_call_handler, service_starts_handler, as_standalone=as_standalone)


if __name__ == "__main__":
    start()
