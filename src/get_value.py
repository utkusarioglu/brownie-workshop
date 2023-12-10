#!/home/python/venv/main/bin/python

from instance import get_instance


def main():
    instance = get_instance()
    response = instance.functions.getValueStorage().call()
    print(response)


if __name__ == "__main__":
    main()
