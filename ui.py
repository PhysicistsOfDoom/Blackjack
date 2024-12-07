import pygame
from main import screen, BLACK, WHITE, font


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
    pygame.draw.rect(screen, "red", [245,495, 310, 210], 3, 5)

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