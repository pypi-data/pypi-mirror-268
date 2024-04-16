import ipih


def start() -> None:
    from PolibaseService.service import start

    start(True)


if __name__ == "__main__":
    start()
