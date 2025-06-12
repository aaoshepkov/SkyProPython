def get_mask_card_number(card_num: str) -> str:
    """Функция принимает на вход номер карты в виде числа
    и возвращает маску номера по правилу
    XXXX XX** **** XXXX
    """
    return f"Номер карты {card_num[:4]} {card_num[4:6]}** **** {card_num[12:]}"


def get_mask_account(acc_num: str) -> str:
    """
    Функция принимает номер счета и приводит его к виду **XXXX
    :param acc_num: строка 20 символов
    :return: строка вида **XXXX
    """
    return f"Номер счета **{acc_num[-4:]}"
    # else:
    #     return f"Вы ввели {len(acc_num)} цифр(ы). Нужно ввести 20 цифр"
