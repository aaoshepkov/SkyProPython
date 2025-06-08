from typing import Any, Dict, List


def filter_by_currency(dct, cur):
    """
    Фильтрует транзакцию по коду(виду) валюты
    :param dct: передается список, содержащий в себе словари с данными транзакций
    :param cur: код валюты, по которому будет производиться фильтрация
    :return:
    """
    return (x for x in dct if x.get("operationAmount").get("currency").get("code") == cur)


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
