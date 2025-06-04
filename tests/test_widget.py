import pytest
from src.widget import mask_account_card
from src.widget import get_date


@pytest.mark.parametrize('num,  expected', [
    ("4016223056204055", "Номер карты 4016 22** **** 4055"),
    ("25016202562348900001", "Номер счета **0001")
    ])
def test_widget(num, expected):
    assert mask_account_card(num) == expected


@pytest.mark.parametrize("date, expected", [("")])
def test_get_date(date, expected):
    assert get_date(date) == expected