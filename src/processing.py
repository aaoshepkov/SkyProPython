from datetime import datetime


def filter_by_state(dict_list: list, state='CANCELED') -> list:
    '''

    :param dict_list: a list of dictionaries
    :param state: by default is 'EXECUTED'
    :return: a list of dictionaries, where the keys are equal to 'state'
    '''
    new_list = []
    for i in dict_list:
        for key, value in i.items():
            if key == 'state' and value == state:
                new_list.append(i)
    return new_list

print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))


def sort_by_date(dict_list: list, sorting='desc') -> list:
    if sorting == 'desc':
        sorted_dict_list = sorted(dict_list, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    elif sorting == 'asc':
        sorted_dict_list = sorted(dict_list, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=False)
    return sorted_dict_list
print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], 'desc'))