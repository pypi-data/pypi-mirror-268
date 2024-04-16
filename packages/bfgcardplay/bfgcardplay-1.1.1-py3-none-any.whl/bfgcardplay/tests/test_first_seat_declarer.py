from .. import next_card
from ..tests.utilities import get_boards


boards = get_boards('first_seat_declarer.pbn')


def test_select_suit_with_cards():
    board = boards['0']
    next_card(board).name  # Seem to need to play this card before we get the correct card
    assert next_card(board).name[1] != 'D'


def test_select_suit_with_winners_in_partners_hand():
    board = boards['1']
    assert next_card(board).name[1] == 'S'


def test_do_not_play_losers_when_you_have_winners():
    board = boards['2']
    assert next_card(board).suit.name != 'C'
