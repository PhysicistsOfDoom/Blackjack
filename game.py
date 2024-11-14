from sys import exit
from table import Deck, Dealer, Player
"""
- This module is where we handle all the functionalities in the U.I, pygame will handle the visuals
- We will use the classes from the table module to handle the game logic
"""

def main():
    deck = Deck() #List of tuples of random cards
    
    #Initialize players
    player = Player()
    dealer = Dealer()

    #Begin Game (Y/N)
    begin = input("Want to begin? (Y/N)")
    if begin.lower() == "y":
        running = True
    else:
        exit()
    
    #Game Loop
    while running:
        #Deal cards to player and dealer
        for _ in range(2):
            player.recieve_card(deck.deal_cards())
            dealer.recieve_card(deck.deal_cards())

        #Show cards to table
        print(f'Player: {player.hand}\n Player Score: {player.calculate_score()}' )
        print(f'Dealer: {dealer.hand}\n Dealer Score: {dealer.calculate_score()}')

        #Ask to Hit or Stand. If hit, give player a new card
        player_decision = input("Hit or Stand? (Y/N)")
        if player_decision.lower() == "y":
            player.recieve_card(deck.deal_cards())

        #Automatically hit for dealer if score is less than 17
        dealer.must_hit(deck.deal_cards())

        #Recalculate scores
        print(f'Player: {player.hand}\n Player Score: {player.calculate_score()}' )
        print(f'Dealer: {dealer.hand}\n Dealer Score: {dealer.calculate_score()}')

        running = False

if __name__ == "__main__":
    main()