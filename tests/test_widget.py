import pytest
from src.widget import mask_account_card


@pytest.mark.parametrize('num,  expected', [("4016223056204055", "Номер карты 4016 22** **** 4055"), ("2501620256234890001", "Номер счета **0001")])
def test_widget(num, expected):
    assert mask_account_card(num) == expected