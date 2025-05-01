from datetime import datetime


from mypy.types import AnyType


def filter_by_state(transactions_list: list[dict[str, AnyType]], state: str = "EXECUTED") -> list:
    """
    :param transactions_list: a list of dictionaries(transactions with id, state, date)
    :param state: optional param, by default is 'EXECUTED'
    :return: a list of filtered dictionaries, where the keys are equal to 'state'
    """
    filtered_list = []
    for transaction in transactions_list:
        for key, value in transaction.items():
            if key == "state" and value == state:
                filtered_list.append(transaction)
    return filtered_list


def sort_by_date(transactions_list: list, sorting_asc: bool = True) -> list:
    """
    :param transactions_list: a list of dictionaries(transactions with id, state, date)
    :param sorting_asc: if True, sorts from newer to older. If False, sorts from older to newer transaction.
    :return: a sorted list of dictionaries, according to params
    """
    if sorting_asc is True:
        return sorted(
            transactions_list, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=False
        )
    elif sorting_asc is False:
        return sorted(
            transactions_list, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True
        )
