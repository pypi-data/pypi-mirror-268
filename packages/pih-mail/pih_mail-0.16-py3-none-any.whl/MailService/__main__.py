import ipih


def start() -> None:
    from MailService.service import start

    start(True)


if __name__ == "__main__":
    start()
