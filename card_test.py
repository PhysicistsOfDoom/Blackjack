import pygame
from cards import cards_to_paths
from logic import Deck

#Beginning
pygame.init()
screen = pygame.display.set_mode((800, 600))

deck = Deck()

#Get Random Card from original deck
card = deck.original_deck[0]  

# Load the card image
file_path = cards_to_paths[card] #File Path from card to image path
card_image = pygame.transform.scale(pygame.image.load(file_path), (150, 200)) # (Image Surface, Size)


# Blit the image to the screen
screen.fill((0, 128, 0))  # Green background
screen.blit(card_image, (100, 100))  # Position the card
pygame.display.flip()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()