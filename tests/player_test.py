import pytest
from table import Player, Deck

#Test initialization
def test_player_initialization():
    player1 = Player()
    assert player1.name == "player"
    assert player1.hand == []
    assert player1.score == 0
    assert player1.wins == []

#Test recieving cards
def test_player_recieve_cards():
    player1 = Player()
    player1.recieve_card()
    assert len(player1.hand) == 1

#Test reset hands 
def test_player_reset_hand():
    player1 = Player()
    for _ in range(4):
        player1.recieve_card()
    player1.reset_hand()
    assert len(player1.hand) == 0