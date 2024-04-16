from .. import next_card
from ..tests.utilities import get_boards


boards = get_boards('fourth_seat_defender.pbn')


def test_play_partners_suit():
    """Ensure notdiscard a winner."""
    board = boards['0']
    assert next_card(board).name != 'QC'
