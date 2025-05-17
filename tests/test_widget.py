import pytest
import src.widget
from tests.conftest import mask_account_card_data


@pytest.mark.parametrize('num,  expected', )
def test_widget(mask_account_card_data):
    assert src.widget.mask_account_card(mask_account_card_data()) == 0