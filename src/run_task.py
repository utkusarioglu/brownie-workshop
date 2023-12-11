#!/home/python/venv/main/bin/python

from sys import argv
from src.tasks import (
    set_sample_value,
    get_sample_value,
    deploy_sample_contract,
)


def main(command: str, values: any):
    match command:
        case "deploy":
            return deploy_sample_contract.delay()
        case "set":
            return set_sample_value.delay(*values)
        case "get":
            return get_sample_value.delay()


if __name__ == "__main__":
    command = argv[1]
    values = [int(v) for v in argv[2:]]
    main(command, values)
