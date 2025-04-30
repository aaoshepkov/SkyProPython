from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_acc_num: str) -> str:
    """
    mask_account_card
    :param card_or_acc_num: принимает на вход строку с номером карты, либо номером счета
    :return: возвращает маскированный номер карты или номер счета (маскировка производится модулем masks.py)
    """
    acc_num = card_or_acc_num.split()
    for num in acc_num:
        if num.isdigit() and len(num) == 16:
            return get_mask_card_number(num)
    # if len(acc_num) == 16:
    #     return get_mask_card_number(acc_num)
    # elif len(acc_num) == 20:
    #     return get_mask_account(acc_num)
    # else:
    #     return "Номер должен содержать 16 (карта) или 20 (счет) цифр"


def get_date(date: str) -> str:
    """
    обрабатывает строку с датой и временем и переводит ее в формат dd.mm.yyyy
    :param date: строка вида "2024-03-11T02:26:18.671407"
    :return: строка вида "11.03.2024"
    """
    date_formatted = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    return date_formatted.strftime("%d.%m.%Y")
print(get_mask_account("Visa Platinum 7000792289606361"))

#комментарий для коммита в новую ветку