from .. import next_card
from ..tests.utilities import get_boards


boards = get_boards('second_seat_defender.pbn')


def test_play_partners_suit():
    """Do not play high card when inappropriate."""
    board = boards['0']
    assert next_card(board).name != 'KH'
