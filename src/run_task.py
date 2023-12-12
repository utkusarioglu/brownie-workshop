#!/home/python/venv/main/bin/python

from typing import Union
from sys import argv
from src.worker.app import (
    set_sample_value,
    get_sample_value,
    deploy_sample_contract,
)

Values = list[Union[int, str]]


def main(command: str, values: Values):
    match command:
        case "deploy":
            return deploy_sample_contract.delay()
        case "set":
            return set_sample_value.delay(*values)
        case "get":
            return get_sample_value.delay()


if __name__ == "__main__":
    command = argv[1]
    values: Values = [int(v) for v in argv[2:]]
    main(command, values)
