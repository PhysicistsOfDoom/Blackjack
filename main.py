import pygame
from pygame.locals import *
from sys import exit
from logic import *
import time
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

    #Menu
    def draw_menu():
        #Fill color screen
        screen.fill((BLACK))

        #Buttons to return
        buttons_list = []

        #Buttons (initial position, width, height)
        start_button = pygame.Rect(0,0, 300, 200) #Start Button
        start_button.center = (400,200)
        quit_button = pygame.Rect(0,0, 300, 200) #Quit Button
        quit_button.center = (400,600)
        buttons_list.append(start_button) #0
        buttons_list.append(quit_button) #1
        
        
        #Draw To Screen
        pygame.draw.rect(screen, WHITE, start_button)
        pygame.draw.rect(screen, WHITE, quit_button)
        pygame.draw.rect(screen, "green", [245,95, 310, 210], 3, 5)

        #Text
        start_text = font.render("Play BlackJack", True, BLACK)
        quit_text = font.render("Quit Game", True, BLACK)
        start_text_rect = start_text.get_rect(center=start_button.center)
        quit_text_rect = quit_text.get_rect(center=quit_button.center)

        #Blit Text
        screen.blit(start_text, start_text_rect)
        screen.blit(quit_text, quit_text_rect)

        return buttons_list

    #Play
    def draw_game():
        #Color Screen
        screen.fill((1,50,32))

        #Button List for Outside Use
        button_list = []

        #Buttons
        return_button = pygame.Rect(0,0, 100, 50) #Return to Menu Button
        return_button.center = (75,50)
        hit_button = pygame.Rect(0,0, 100, 50) #Hit Button
        hit_button.center = (75,700)
        stand_button = pygame.Rect(0,0, 100, 50) #Stand Button
        stand_button.center = (725,700)
        button_list.append(hit_button) #0
        button_list.append(stand_button) #1
        button_list.append(return_button) #2
        
        #Return Button
        pygame.draw.rect(screen, WHITE, return_button)
        return_text = font.render("Menu", True, BLACK)
        return_text_rect = return_text.get_rect(center=return_button.center)
        screen.blit(return_text, return_text_rect)

        #Hit Button
        pygame.draw.rect(screen, WHITE, hit_button)
        hit_text = font.render("HIT!", True, BLACK)
        hit_text_rect = hit_text.get_rect(center=hit_button.center)
        screen.blit(hit_text, hit_text_rect)

        #Stand Button
        pygame.draw.rect(screen, WHITE, stand_button)
        stand_text = font.render("STAND!", True, BLACK)
        stand_text_rect = stand_text.get_rect(center=stand_button.center)
        screen.blit(stand_text, stand_text_rect)

        return button_list

    '--------------------------------------------------Game Loop Code------------------------------------------------'

    #Run Loop
    running = True
    hit_stand_loop = True

    #Game state
    in_game = False

    #Intialize Values First
    player = Player()
    dealer = Dealer()
    deck = Deck() #List of tuples of random cards

    #Game Loop
    while running:

        #FPS, Updating Display & Draw
        clock.tick(60)
        #Draw Whatever is Active
        if not in_game:
            menu_buttons = draw_menu() #[Start, Quit]
        if in_game:
            game_buttons = draw_game() #[Hit, Stand, Return]
        
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