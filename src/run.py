#!/home/python/venv/main/bin/python

from sys import argv
from tasks import add


def main(values: list[int]):
    return add.delay(*values)


if __name__ == "__main__":
    values = [int(v) for v in argv[1:]]
    main(values)
