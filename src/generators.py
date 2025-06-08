from typing import List, Dict, Any, Iterator

transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

def filter_by_currency(dct, cur):
    """
    Фильтрует транзакцию по коду(виду) валюты
    :param dct: передается список, содержащий в себе словари с данными транзакций
    :param cur: код валюты, по которому будет производиться фильтрация
    :return:
    """
    return (x for x in dct if x.get("operationAmount").get("currency").get("code") == cur)

# usd_transactions = filter_by_currency(transactions, "USD")
# try:
#     for _ in range(5):
#         print(next(usd_transactions))
# except StopIteration:
#     print("Транзакций больше нет")


def transaction_descriptions(dct: List[Dict[Any, Any]]):
    """
    Получаем описание транзакций
    :param dct: передается список, содержащий в себе словари с данными транзакций
    :return: Описание (значение по ключу "description")
    """
    return (x["description"] for x in dct if "description" in x)


def card_number_generator(start: int, end: int):
    """
    Генерирует номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999
    :param start: указать начало диапазона
    :param end: указать конец диапазона
    :return:
    """
    current = start
    while current <= end:
        # Форматируем число в 16-значную строку с ведущими нулями
        card_num = f"{current:016d}"
        # Разбиваем на группы по 4 цифры и объединяем через пробел
        formatted_num = ' '.join([card_num[i:i+4] for i in range(0, 16, 4)])
        yield formatted_num
        current += 1
