from sys import exit
import random
import time
import pygame
from pygame.locals import *


"""
- This module is where we hold the Deck for shuffling and managing used cards.
- Establishing Players and handling their hands
- Dealing the players and managing the Dealers hand.
"""

#PNG to BlackJack Cards

#Classes
class Deck:
    def __init__(self):
        self.rank = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, "J", "K", "Q", "A"]
        self.suit = ["♣", "♦", "♥", "♠"]
        self.original_deck = [(r,s) for r in self.rank for s in self.suit]
        random.shuffle(self.original_deck) #This just shuffles the entire deck
        self.deck = self.original_deck[:] * 4 #Make a Copy & Multiply it by 4 so we have 4 Decks to avoid Card Loss

    def deal_cards(self):
        return self.deck.pop()
    
    #reset the deck so we dont run out of cards during the loop.
    def reset_deck(self):
        self.__init__()


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

#Functions
def show_player_cards(player, screen):
    player_cards = ", ".join([f"{rank}{suit}" for rank, suit in player.hand])
    font = pygame.font.Font(None, 36)
    player_card_surface = font.render(player_cards, True, (255,255,255))
    player_card_rect = player_card_surface.get_rect(center=(200,600))
    screen.blit(player_card_surface, player_card_rect)

#Show Dealer Cards
def show_dealer_cards(dealer, screen):
    dealer_cards = ", ".join([f"{rank}{suit}" for rank, suit in dealer.hand])
    font = pygame.font.Font(None, 36)
    dealer_cards_surface = font.render(dealer_cards, True, (255,255,255))
    dealer_cards_rect = dealer_cards_surface.get_rect(center=(200,200))
    screen.blit(dealer_cards_surface, dealer_cards_rect)

#Compare score per hit/stand
def compare_score(player, dealer):
    if player.calculate_score() == 21:
        print("Player got a Blackjack! Player wins!")
        player.wins += 1

    elif dealer.calculate_score() == 21:
        print("Dealer got a Blackjack! Dealer wins!")
        dealer.wins += 1

    #Check if either bust over 21
    if player.calculate_score() > 21:
        print("Player busts! Dealer wins!")
        dealer.wins += 1

    elif dealer.calculate_score() > 21:
        print("Dealer busts! Player wins!")
        player.wins += 1


def handle_menu(event, player, dealer, deck):
        # Initialize the game
        player.reset_hand()
        dealer.reset_hand()
        deck.reset_deck()
        for _ in range(2):
            player.recieve_card(deck.deal_cards())
            dealer.recieve_card(deck.deal_cards())
