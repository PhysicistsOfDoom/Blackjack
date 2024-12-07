import pygame
from pygame.locals import *
from sys import exit
from logic import *
from ui import *
import time
from cards import cards_to_paths
"""
Welcome to Blacjack built in pygame, this is a less functional but still playable game of blacjack
- Other modules connected like game.py handle the functionality and rules.
- logic.py holds the players hands, handles the decks leftovers and the dealers actions
- This module uses the pygame U.I in ui.py to establish a better experience

Date: 11/14/2024
Github: PhysicistsOfDoom
By: Corbin T
"""

#initialize 
pygame.init()

#window
screen = pygame.display.set_mode((800, 800))
screen_x, screen_y = screen.get_size()
screen.fill((1,50,32))

#Caption, Icon & Font
font = pygame.font.Font(None, 36)
icon = pygame.image.load("./media/UVU.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("UVU Blackjack")

#clock
clock = pygame.time.Clock()

#Colors
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)

def main():
    #Local Variables
    running = True
    hit_stand_loop = True
    in_game = False
    dealed_cards = False

    #Intialize Values First
    player = Player()
    dealer = Dealer()
    deck = Deck() #List of tuples of random cards

    '''---------------------------------------------- GAME LOOP BELOW --------------------------------------------------'''

    #Game Loop
    while running:

        #FPS, Updating Display & Draw
        clock.tick(60)
        #Draw Whatever is Active
        if not in_game:
            menu_buttons = draw_menu() #[Start, Quit]
            dealed_cards = False
        if in_game:
            game_buttons = draw_game() #[Hit, Stand, Return]
            if not dealed_cards: #Check if cards aren't dealt yet
                #Deal Cards
                deal_first_cards(player, dealer, deck)
                print(player.hand)
                print(dealer.hand)

                #Get each card from hand
                player_card_1 = player.hand[0] #pick a card
                player_card_2 = player.hand[1] #pick a card
                dealer_card_1 = dealer.hand[0] #pick a card
                dealer_card_2 = dealer.hand[1] #pick a card

                #Get each cards filepath
                player1_file_path = cards_to_paths[player_card_1] #this gets the file path of the card
                player2_file_path = cards_to_paths[player_card_2] #this gets the file path of the card
                dealer1_file_path = cards_to_paths[dealer_card_1] #this gets the file path of the card
                dealer2_file_path = cards_to_paths[dealer_card_2] #this gets the file path of the card

                #Generate image for cards
                player1_card_image = pygame.transform.scale(pygame.image.load(player1_file_path), (150, 200)) # (Image Surface, Size) #load the card image
                player2_card_image = pygame.transform.scale(pygame.image.load(player2_file_path), (150, 200)) # (Image Surface, Size) #load the card image
                dealer1_card_image = pygame.transform.scale(pygame.image.load(dealer1_file_path), (150, 200)) # (Image Surface, Size) #load the card image
                dealer2_card_image = pygame.transform.scale(pygame.image.load(dealer2_file_path), (150, 200)) # (Image Surface, Size) #load the card image


                #Finish Dealing Cards
                dealed_cards = True
        
            #Display The Cards
            if hit_stand_loop:
                screen.blit(player1_card_image, (200,70))
                screen.blit(player2_card_image, (300,60))
                screen.blit(dealer1_card_image, (200,400))
                screen.blit(dealer2_card_image, (300,390))


        #Event Handle
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                exit()

            #Menu & Play Screen Mechanics
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not in_game:
                    if menu_buttons[0].collidepoint(event.pos):
                        #Initialize Players, Dealer & Deck
                        in_game = True
                        #Setup Game
                        handle_menu(event, player, dealer, deck)

                    elif menu_buttons[1].collidepoint(event.pos):
                        running = False
                elif in_game:
                    if game_buttons[2].collidepoint(event.pos):
                        in_game = False


        #Update Screen
        pygame.display.update()

if __name__ == "__main__":
    main()