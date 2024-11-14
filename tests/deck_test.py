from table import Deck

#Just want to see if 52 cards are present in the deck
def test_deck_initilizer():
    deck = Deck()
    assert len(deck.cards) == 52 

#Test Shuffling
def test_deck_shuffle():
    deck1 = Deck()
    deck2 = Deck()
    assert deck1.deck != deck2.deck

#Test Deck dealing
def test_deck_deal():
    deck = Deck()
    initial_len = len(deck.deck)
    deck.deal_cards()
    assert initial_len != len(deck.deck)