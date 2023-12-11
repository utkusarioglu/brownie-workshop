from src.instance import get_instance


def get_value():
    instance = get_instance()
    response = instance.functions.getValueStorage().call()
    return response
