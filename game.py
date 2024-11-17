from sys import exit
from table import Deck, Dealer, Player
"""
- This module is where we handle all the functionalities in the U.I, pygame will handle the visuals
- We will use the classes from the table module to handle the game logic
"""

def main():

    #Start the game:
    begin = input("Start? (Y/N)")
    if begin.lower() == "y":
        running = True
    else:
        running = False
        exit()

    #Initialize Players, Dealer & Deck
    player = Player()
    dealer = Dealer()
    deck = Deck() #List of tuples of random cards
    
    #Game Loop
    while running:

        #Menu Screen
        in_menu = True
        while in_menu:
            print("\nMenu:")
            menu_choices = int(input("""
            1. Play Blackjack
            2. Check Player Wins
            3. Check Dealer Wins
            4. Exit
            """))

            if menu_choices == 1:
                in_menu = False
                break
            elif menu_choices == 2:
                print(f"Player Wins: {player.wins}")
            elif menu_choices == 3:
                print(f"Dealer Wins: {dealer.wins}")
            else:
                print(f"\n Thanks for Playing!")
                running = False
                exit()

        #Reset players hands:
        player.reset_hand()
        dealer.reset_hand()

        #Deal cards to player and dealer
        for _ in range(2):
            player.recieve_card(deck.deal_cards())
            dealer.recieve_card(deck.deal_cards())

        #Show initial cards & scores to table
        print(f'Player: {player.hand}\n Player Score: {player.calculate_score()}' )
        print(f'Dealer: {dealer.hand}\n Dealer Score: {dealer.calculate_score()}\n')

        #Check if either got a Blackjack on first go.
        if player.calculate_score() == 21:
            print("Player got a Blackjack! Player wins!")
            player.wins += 1
            running = False
            continue
        elif dealer.calculate_score() == 21:
            print("Dealer got a Blackjack! Dealer wins!")
            dealer.wins += 1
            running = False
            continue


        #Start the hit or stand loop until someone either blacjacks, wins, loses or busts > 21.
        hit_stand_loop = True
        while hit_stand_loop:        
            #Ask to Hit or Stand
            player_decision = input("Hit or Stand? (Y/N)")

            #Player Hits
            if player_decision.lower() == "y":
                player.recieve_card(deck.deal_cards())


                #Check If Player Busts.
                if player.calculate_score() > 21:
                    print(f'\nPlayer: {player.hand}\n Player Score: {player.calculate_score()}')
                    print(f'Dealer: {dealer.hand}\n Dealer Score: {dealer.calculate_score()}')
                    print("\n BUST! Dealer Wins!")
                    dealer.wins += 1
                    hit_stand_loop = False #Stop The Hit Loop

                #No Bust.
                else:
                    #Display Updated Scores.
                    print(f'Player: {player.hand}\n Player Score: {player.calculate_score()}')
                    print(f'Dealer: {dealer.hand}\n Dealer Score: {dealer.calculate_score()}')


            #Player Stands.
            elif player_decision.lower() == "n":  
                #Dealer Hits While Score < 17.
                while dealer.calculate_score() < 17:
                    dealer.recieve_card(deck.deal_cards())

                #Show Final Scores
                print(f'\nPlayer: {player.hand}\n Player Score: {player.calculate_score()}')
                print(f'Dealer: {dealer.hand}\n Dealer Score: {dealer.calculate_score()}')

                #Determine The Winner
                if dealer.calculate_score() > 21:
                    print("\nBUST! Player Wins!")
                    player.wins += 1
                elif dealer.calculate_score() > player.calculate_score():
                    print("\nDealer Wins!")
                    dealer.wins += 1
                elif dealer.calculate_score() < player.calculate_score():
                    print("\nPlayer Wins!")
                    player.wins += 1
                else:
                    print("\nIt's a Tie!")
                
                hit_stand_loop = False  #End the hit/stand loop

if __name__ == "__main__":
    main()