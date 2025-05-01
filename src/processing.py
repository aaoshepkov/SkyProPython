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
        if transaction.get('state') == state:
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
print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))