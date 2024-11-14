import random
"""
- This module is where we hold the Deck for shuffling and managing used cards.
- Establishing Players and handling their hands
- Dealing the players and managing the Dealers hand.
"""


class Deck:
    def __init__(self):
        self.rank = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, "J", "K", "Q", "A"]
        self.suit = ["♣", "♦", "♥", "♠"]
        self.deck = [(r,s) for r in self.rank for s in self.suit]
        random.shuffle(self.deck) #This just shuffles the entire deck

    def deal_cards(self):
        return self.deck.pop()
    

class Player(Deck):
    def __init__(self, name="player"):
        self.name = name
        self.hand = []
        self.score = 0
        self.wins = 0

    #Method to recieve a card
    def recieve_card(self, card):
        self.hand.append(card)

    def show_card(self):
        return self.hand
    
    def reset_hand(self):
        self.hand = []


    #Method to calculate scores according to card
    def calculate_score(self):
        self.score = 0
        for card, suit in self.hand:
            if card in ["J", "Q", "K"]:
                self.score += 10
            elif card == "A":
                self.score += 11
            else:
                self.score += card
        return self.score


class Dealer(Player):
    def __init__(self):
        super().__init__(name="dealer") #Inherit all the essentials from Player
        self.wins = 0

    def must_hit(self, cards):
        while self.calculate_score() < 17:
            self.recieve_card(cards)
    
    def show_card(self):
        return self.hand
    