import pygame
from sys import exit
import game, table
"""
Welcome to Blacjack built in pygame, this is a less functional but still playable game of blacjack
- Other modules connected like game.py handle the functionality and rules.
- table.py holds the players hands, handles the decks leftovers and the dealers actions
- This module holds the pygame U.I to establish a better experience

Date: 11/14/2024
By: Corbin Thomas Beus
Github: PhysicistsOfDoom
"""

def main():
    #Initializer, Display, Caption, Clock
    pygame.init()
    screen = pygame.display.set_mode((800, 400)) #Display Surface
    pygame.display.set_caption("Blackjack") #Screen title
    fps = pygame.time.Clock()


    # Varaibles
    sky_surface = pygame.Surface((800, 350)) #regular surface to blit on the display surface
    sky_surface.fill('Blue')

    ground = pygame.Surface((800, 50)) #ground regular surface
    ground.fill("Green")

    test_font = pygame.font.Font(None, 50) #text to display 
    text_surf = test_font.render("Hello", False, "White") #rendering the text
    text_rect = text_surf.get_rect(center=(400, 50))

    player = pygame.Surface((50,50)) #regular surface player
    player.fill("Black")
    player_rect = player.get_rect(midbottom = (400, 350)) #wrapping the player surface in a rect to give it easier function and perks

    threat_surf = pygame.Surface((50, 50)) #Threat regular surface to test collision
    threat_surf.fill("White")
    threat_rect = threat_surf.get_rect(midbottom = (100, 350)) #


    while True:
        #check input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() #stops the pygame modules
                exit() #closes the loop
            if event.type == pygame.MOUSEMOTION:
                if player_rect.collidepoint(event.pos): 
                    player.fill("Red")


        screen.blit(sky_surface, (0,0)) #blitting the test_surface onto the display surface
        screen.blit(ground, (0, 350)) #blitting the ground surface onto the floor
        screen.blit(text_surf, text_rect)
        screen.blit(player, player_rect)

        screen.blit(threat_surf, threat_rect)

        
        pygame.display.update() #updates the screen after all input events have changed.
        fps.tick(60) #frame every 1/60 second.


if __name__ == "__main__":
    main()