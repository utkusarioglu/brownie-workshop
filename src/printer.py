from pprint import PrettyPrinter


class Printer:
    pp = PrettyPrinter()

    @staticmethod
    def pretty(message: str) -> None:
        Printer.pp.pprint(message)

    @staticmethod
    def print(message: str) -> None:
        print(message)
