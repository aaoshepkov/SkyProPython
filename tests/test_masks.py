import pytest
from src.masks import get_mask_card_number
from src.masks import get_mask_account


@pytest.fixture
def correct_card_number():
    return '4016223056204055'


@pytest.fixture
def correct_account_number():
    return "2501620256234890001"


def test_get_mask_card_number(correct_card_number):
    '''
    Testing masking a correct card number
    :param correct_card_number: '4016223056204055'
    :return: test has to be in PASSED status
    '''
    assert get_mask_card_number(correct_card_number) == 'Номер карты 4016 22** **** 4055'


def test_get_mask_account(correct_account_number):
    '''
    Testing masking a correct account number
    :param correct_card_number: '2501620256234890001'
    :return: test has to be in PASSED status
    '''
    assert get_mask_account(correct_account_number) == "Номер счета **0001"
