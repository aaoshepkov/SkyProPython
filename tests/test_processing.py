from src.processing import filter_by_state
from tests.conftest import filter_by_state_data


def test_filter_by_state():
    assert (filter_by_state(filter_by_state_data) ==
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])
