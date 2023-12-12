from .instance import get_instance


def set_value(new_value: int) -> None:
    instance = get_instance()
    transaction = instance.functions.setValue(new_value).transact()
    return transaction
