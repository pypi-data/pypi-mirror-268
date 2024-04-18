import ipih


def start() -> None:
    from IOTDevicesService.service import start

    start(True)


if __name__ == "__main__":
    start()
