#!/home/python/venv/main/bin/python

from sys import argv
from printer import Printer
from instance import get_instance


def main(new_value: int) -> None:
    instance = get_instance()
    transaction = instance.functions.setValue(new_value).transact()
    Printer.pretty(transaction)


if __name__ == "__main__":
    new_value = int(argv.pop())
    main(new_value)
