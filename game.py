from sys import exit
from table import Deck, Dealer, Player
"""
- This module is where we handle all the functionalities in the U.I, pygame will handle the visuals
- We will use the classes from the table module to handle the game logic
"""

def main():
    #Begin Game (Y/N)
    begin = input("Want to begin? (Y/N)")
    if begin.lower() == "y":
        running = True
        hit_stand_loop = True
    else:
        exit()

    #Initialize Players, Dealer & Deck
    player = Player()
    dealer = Dealer()
    deck = Deck() #List of tuples of random cards
    
    #Game Loop
    while running:
        #Reset players hands:
        player.reset_hand()
        dealer.reset_hand()

        #Deal cards to player and dealer
        for _ in range(2):
            player.recieve_card(deck.deal_cards())
            dealer.recieve_card(deck.deal_cards())

        #Show cards to table
        print(f'Player: {player.hand}\n Player Score: {player.calculate_score()}' )
        print(f'Dealer: {dealer.hand}\n Dealer Score: {dealer.calculate_score()}\n')

        #Check if either got a Blackjack on first go.
        if player.hand == 21:
            print("Player got a Blackjack! Player wins!")
            player.wins += 1
        elif dealer.hand == 21:
            print("Dealer got a Blackjack! Dealer wins!")
            dealer.wins += 1


        #Start the hit or stand loop until someone either blacjacks, wins, loses or busts > 21.
        while hit_stand_loop:        
            #Ask to Hit or Stand. If hit, give player a new card
            player_decision = input("Hit or Stand? (Y/N)")

            # If the player chooses HIT, then run and calculate
            if player_decision.lower() == "y":

                player.recieve_card(deck.deal_cards())
                #Bust calculation
                if player.calculate_score() > 21:
                    print(f'\nPlayer: {player.hand}\n Player Score: {player.calculate_score()}')
                    print(f'Dealer: {dealer.hand}\n Dealer Score: {dealer.calculate_score()}')
                    print("\n BUST! Dealer Wins!")
                    dealer.wins += 1
                    hit_stand_loop = False
                else:
                    print(f'Player: {player.hand}\n Player Score: {player.calculate_score()}')
                    print(f'Dealer: {dealer.hand}\n Dealer Score: {dealer.calculate_score()}')

            # If the player chooses no, run the dealers turn
            if player_decision.lower() == "n":

                #Automatically hit for dealer if score is less than 17
                dealer.must_hit(deck.deal_cards())

                #Check if the dealer went over 21.
                if dealer.calculate_score() > 21:
                    print(f'Player: {player.hand}\n Player Score: {player.calculate_score()}')
                    print(f'Dealer: {dealer.hand}\n Dealer Score: {dealer.calculate_score()}')
                    print("\n BUST! Player Wins!")
                    player.wins += 1
                    hit_stand_loop = False
                hit_stand_loop = False


        running = False


if __name__ == "__main__":
    main()