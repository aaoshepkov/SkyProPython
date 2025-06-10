import pytest
from src.decorators import log


def successful_func(a, b):
    return a + b


def failing_func(a, b):
    return a / b


@pytest.mark.parametrize(
    "func,args,kwargs,expected_output",
    [
        (successful_func, (2, 3), {}, "Результат: 5"),
        (successful_func, (5, -1), {}, "Результат: 4"),
        (failing_func, (10, 0), {}, "ZeroDivisionError"),
    ]
)
def test_log_console_output(capsys, func, args, kwargs, expected_output):
    decorated_func = log()(func)

    try:
        decorated_func(*args, **kwargs)
    except Exception:
        pass

    captured = capsys.readouterr()
    assert expected_output in captured.out
    assert f"Аргументы: {args}" in captured.out


@pytest.mark.parametrize(
    "func,args,kwargs,expected_content",
    [
        (successful_func, (3, 4), {}, "Результат: 7"),
        (failing_func, (8, 0), {}, "ZeroDivisionError"),
    ]
)
def test_log_file_output(tmp_path, func, args, kwargs, expected_content):
    # Создаем временный файл для теста
    log_file = tmp_path / "test.log"

    decorated_func = log(filename=str(log_file))(func)

    try:
        decorated_func(*args, **kwargs)
    except Exception:
        pass

    assert log_file.exists()
    content = log_file.read_text(encoding="utf-8")
    assert expected_content in content
    assert f"Аргументы: {args}" in content


@pytest.mark.parametrize(
    "exception_type,error_message",
    [
        (ValueError, "Неверное значение"),
        (TypeError, "Несовместимые типы"),
    ]
)
def test_exception_propagation(exception_type, error_message):
    def func():
        raise exception_type(error_message)

    decorated_func = log()(func)

    with pytest.raises(exception_type) as exc_info:
        decorated_func()

    assert str(exc_info.value) == error_message
