from src.masks import get_mask_account, get_mask_card_number
from tests.conftest import correct_card_number


def test_get_mask_card_number(correct_card_number: str) -> None:
    """
    Testing masking a correct card number
    :param correct_card_number: '4016223056204055'
    :return: test has to be in PASSED status
    """
    assert get_mask_card_number(correct_card_number) == "Номер карты 4016 22** **** 4055"


def test_get_mask_account(correct_account_number: str) -> None:
    """
    Testing masking a correct account number
    :param correct_card_number: '2501620256234890001'
    :return: test has to be in PASSED status
    """
    assert get_mask_account(correct_account_number) == "Номер счета **0001"
