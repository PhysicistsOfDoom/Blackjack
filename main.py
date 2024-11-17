import pygame
from pygame.locals import *
from sys import exit
import game, table
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
    screen = pygame.display.set_mode((800, 500))
    screen_x, screen_y = screen.get_size()

    #Caption & Icon
    icon = pygame.image.load("./media/UVU.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("UVU Blackjack")

    #clock
    clock = pygame.time.Clock()

    '--------------------------------------------------Game Loop Code-----------------------------------------------'

    running = True

    #Game Loop
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
                exit()

            #Game mechanics









        #Display & Clock 60 fps
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()