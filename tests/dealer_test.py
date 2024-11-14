import pytest
from table import Dealer

#Test subclass initialization
def test_dealer_init():
    dealer1 = Dealer()
    assert dealer1.name == "dealer"
    assert dealer1.hand == []
    assert dealer1.score == 0
    assert dealer1.wins == 0


#Test recieving cards
def test_dealer_recieve_cards():
    dealer1 = Dealer()
    dealer1.recieve_card()
    assert len(dealer1.hand) == 1

#Test reset hands 
def test_player_reset_hand():
    dealer1 = Dealer()
    for _ in range(4):
        dealer1.recieve_card()
    dealer1.reset_hand()
    assert len(dealer1.hand) == 0

#Test the must_hit method to make sure dealer always hits if their score is below 17.
def test_dealer_must_hit():
    dealer1 = Dealer()
    dealer1.score = 16
    dealer1.must_hit()
    assert dealer1.score != 16