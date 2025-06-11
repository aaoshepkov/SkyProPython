import time
from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Запоминаем время старта
            start_time = time.time()

            try:
                result = func(*args, **kwargs)
                execution_time = time.time() - start_time

                success_message = (
                    f"[{time.ctime()}] Успешный вызов {func.__name__}\n"
                    f"Аргументы: {args}, {kwargs}\n"
                    f"Результат: {result}\n"
                    f"Время выполнения: {execution_time:.4f} сек.\n\n"
                )

                if filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(success_message)
                else:
                    print(success_message)

                return result

            except Exception as e:
                error_message = (
                    f"[{time.ctime()}] Ошибка в функции {func.__name__}\n"
                    f"Аргументы: {args}, {kwargs}\n"
                    f"Тип ошибки: {type(e).__name__}\n"
                    f"Сообщение: {str(e)}\n\n"
                )

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(error_message)
                else:
                    print(error_message)

                raise

        return wrapper

    return decorator
