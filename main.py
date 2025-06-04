import datetime
from src.widget import get_date, mask_account_card


def initial_launch():
    try:
        while True:
            user_input = input('Пожалуйста, введите номер счета или номер карты:\n')
            if len(user_input) == 16 and user_input.isdigit() or len(user_input) == 20 and user_input.isdigit():
                print(mask_account_card(user_input))
            else:
                print("Введенные данные некорректны")

            proceed = input(
                "Если хотите ввести еще один номер карты/счета, напишите: ДА\nИли НЕТ, если хотите завершить\n")
            if proceed.lower() == "да":
                continue
            elif proceed.lower() == "нет":
                return "До свидания!"
    finally:
        current_date = datetime.datetime.now()
        operation_date = str(current_date)
        print(f"Дата операции: {get_date(operation_date)}")



