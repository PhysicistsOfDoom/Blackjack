import pygame
from pygame.locals import *
from sys import exit
from logic import *
"""
Welcome to Blacjack built in pygame, this is a less functional but still playable game of blacjack
- Other modules connected like game.py handle the functionality and rules.
- table.py holds the players hands, handles the decks leftovers and the dealers actions
- This module holds the pygame U.I to establish a better experience

Date: 11/14/2024
Github: PhysicistsOfDoom
By: Corbin T
"""

def main():

    #initialize 
    pygame.init()

    #window
    screen = pygame.display.set_mode((800, 800))
    screen_x, screen_y = screen.get_size()
    screen.fill((1,50,32))

    #Caption & Icon
    icon = pygame.image.load("./media/UVU.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("UVU Blackjack")

    #clock
    clock = pygame.time.Clock()

    #Buttons (initial position, width, height)
    start_button = pygame.Rect(0,0, 300, 200)
    #Final position (x,y)
    start_button.center = (400,200)

    quit_button = pygame.Rect(0,0, 300, 200)
    quit_button.center = (400,600)

    return_button = pygame.Rect(0,0, 100, 50)
    return_button.center = (75,50)

    hit_button = pygame.Rect(0,0, 100, 50)
    hit_button.center = (75,700)

    stand_button = pygame.Rect(0,0, 100, 50)
    stand_button.center = (725,700)

    #Colors
    BLACK = (0,0,0)
    GREEN = (0,255,0)
    RED = (255,0,0)
    WHITE = (255,255,255)

    #Game state
    game_state = "menu"

    #Menu
    def menu():
        #Menu Background Color
        screen.fill((1,50,32))
        
        #Draw To Screen
        pygame.draw.rect(screen, WHITE, start_button)
        pygame.draw.rect(screen, WHITE, quit_button)

        #Text
        font = pygame.font.Font(None, 36)
        start_text = font.render("Play BlackJack", True, BLACK)
        quit_text = font.render("Quit Game", True, BLACK)

        #Text alignment
        start_text_rect = start_text.get_rect(center=start_button.center)
        quit_text_rect = quit_text.get_rect(center=quit_button.center)

        #Blit Text
        screen.blit(start_text, start_text_rect)
        screen.blit(quit_text, quit_text_rect)

    #Play
    def play():
        #Play Background Color
        screen.fill((0,100,50))
        
        #Return Button
        pygame.draw.rect(screen, WHITE, return_button)
        font = pygame.font.Font(None, 20)
        return_text = font.render("Return to Menu", True, BLACK)
        return_text_rect = return_text.get_rect(center=return_button.center)
        screen.blit(return_text, return_text_rect)

        #Hit Button
        pygame.draw.rect(screen, WHITE, hit_button)
        font = pygame.font.Font(None, 30)
        hit_text = font.render("HIT!", True, BLACK)
        hit_text_rect = hit_text.get_rect(center=hit_button.center)
        screen.blit(hit_text, hit_text_rect)

        #Stand Button
        pygame.draw.rect(screen, WHITE, stand_button)
        font = pygame.font.Font(None, 30)
        stand_text = font.render("STAND!", True, BLACK)
        stand_text_rect = stand_text.get_rect(center=stand_button.center)
        screen.blit(stand_text, stand_text_rect)

    '--------------------------------------------------Game Loop Code------------------------------------------------'

    #Run Loop
    running = True

    #Game Loop
    while running:

        #Intialize Values First
        player = Player()
        dealer = Dealer()
        deck = Deck() #List of tuples of random cards

        #Event Handle
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                exit()

            #Menu & Play Screen Mechanics
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_state == "menu":
                    if start_button.collidepoint(event.pos):
                        #Initialize Players, Dealer & Deck
                        game_state = "play" #Start

                    elif quit_button.collidepoint(event.pos):
                        running = False

                elif game_state == "play":
                    if return_button.collidepoint(event.pos):
                        game_state = "menu"

        #Game Mechanics
        player.reset_hand()
        dealer.reset_hand()

        #Deal cards to player and dealer
        for _ in range(2):
            player.recieve_card(deck.deal_cards())
            dealer.recieve_card(deck.deal_cards())

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

        #Check if either bust over 21
        if player.calculate_score() > 21:
            print("Player busts! Dealer wins!")
            dealer.wins += 1
            running = False
            continue
        elif dealer.calculate_score() > 21:
            print("Dealer busts! Player wins!")
            player.wins += 1
            running = False
            continue





        #Check Game state
        if game_state == "menu":
            menu()
        if game_state == "play":
            play()


        #Display & Clock 60 fps
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()