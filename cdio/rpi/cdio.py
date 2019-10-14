import pygame
import time
import gpiozero

pygame.init()

display_width = 800
display_height = 480

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
hiq_rosa = (250, 112, 150)

clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("GodisPong")

largeText = pygame.font.Font('karmatic_arcade.ttf', 90)
smallText = pygame.font.Font('karmatic_arcade.ttf', 60)

button_1 = gpiozero.Button(17) #connected to GPIO17 pin 11, pull-up (UP)
button_2 = gpiozero.Button(27) #connected to GPIO27 pin 13, pull-up (DOWN)
button_3 = gpiozero.Button(22) #connected to GPIO22 pin 15, pull-up (ENTER)
button_4 = gpiozero.Button(23) #connected to GPIO27 pin 16, pull-up (ESC)

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def start_menu_options(option):
    if option == 1:
        
        TextSurf_2, TextRect_2 = text_objects("new game", smallText, red)
        TextRect_2.center = ((display_width / 2), (display_height) * 0.45)
        gameDisplay.blit(TextSurf_2, TextRect_2)

        TextSurf_3, TextRect_3 = text_objects("settings", smallText, black)
        TextRect_3.center = ((display_width / 2), (display_height) * 0.65)
        gameDisplay.blit(TextSurf_3, TextRect_3)

        TextSurf_4, TextRect_4 = text_objects("exit", smallText, black)
        TextRect_4.center = ((display_width / 2), (display_height) * 0.85)
        gameDisplay.blit(TextSurf_4, TextRect_4)  
        
    elif option == 2:

        TextSurf_2, TextRect_2 = text_objects("new game", smallText, black)
        TextRect_2.center = ((display_width / 2), (display_height) * 0.45)
        gameDisplay.blit(TextSurf_2, TextRect_2)

        TextSurf_3, TextRect_3 = text_objects("settings", smallText, red)
        TextRect_3.center = ((display_width / 2), (display_height) * 0.65)
        gameDisplay.blit(TextSurf_3, TextRect_3)

        TextSurf_4, TextRect_4 = text_objects("exit", smallText, black)
        TextRect_4.center = ((display_width / 2), (display_height) * 0.85)
        gameDisplay.blit(TextSurf_4, TextRect_4)  

    elif option == 3:

        TextSurf_2, TextRect_2 = text_objects("new game", smallText, black)
        TextRect_2.center = ((display_width / 2), (display_height) * 0.45)
        gameDisplay.blit(TextSurf_2, TextRect_2)

        TextSurf_3, TextRect_3 = text_objects("settings", smallText, black)
        TextRect_3.center = ((display_width / 2), (display_height) * 0.65)
        gameDisplay.blit(TextSurf_3, TextRect_3)

        TextSurf_4, TextRect_4 = text_objects("exit", smallText, red)
        TextRect_4.center = ((display_width / 2), (display_height) * 0.85)
        gameDisplay.blit(TextSurf_4, TextRect_4)

def game_select_options(game_option):
    if game_option == 1:

        TextSurf_2, TextRect_2 = text_objects("timer", smallText, white)
        TextRect_2.center = ((display_width / 2), (display_height) * 0.3)
        gameDisplay.blit(TextSurf_2, TextRect_2)

        TextSurf_3, TextRect_3 = text_objects("challenge", smallText, black)
        TextRect_3.center = ((display_width / 2), (display_height) * 0.5)
        gameDisplay.blit(TextSurf_3, TextRect_3)

        TextSurf_4, TextRect_4 = text_objects("exit", smallText, black)
        TextRect_4.center = ((display_width / 2), (display_height) * 0.7)
        gameDisplay.blit(TextSurf_4, TextRect_4)  

    elif game_option == 2:

        TextSurf_2, TextRect_2 = text_objects("timer", smallText, black)
        TextRect_2.center = ((display_width / 2), (display_height) * 0.3)
        gameDisplay.blit(TextSurf_2, TextRect_2)

        TextSurf_3, TextRect_3 = text_objects("challenge", smallText, white)
        TextRect_3.center = ((display_width / 2), (display_height) * 0.5)
        gameDisplay.blit(TextSurf_3, TextRect_3)

        TextSurf_4, TextRect_4 = text_objects("exit", smallText, black)
        TextRect_4.center = ((display_width / 2), (display_height) * 0.7)
        gameDisplay.blit(TextSurf_4, TextRect_4)

    elif game_option == 3:

        TextSurf_2, TextRect_2 = text_objects("timer", smallText, black)
        TextRect_2.center = ((display_width / 2), (display_height) * 0.3)
        gameDisplay.blit(TextSurf_2, TextRect_2)

        TextSurf_3, TextRect_3 = text_objects("challenge", smallText, black)
        TextRect_3.center = ((display_width / 2), (display_height) * 0.5)
        gameDisplay.blit(TextSurf_3, TextRect_3)

        TextSurf_4, TextRect_4 = text_objects("exit", smallText, white)
        TextRect_4.center = ((display_width / 2), (display_height) * 0.7)
        gameDisplay.blit(TextSurf_4, TextRect_4)  

def game_select():
    select = True
    game_option = 1

    while select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(hiq_rosa)

        if button_1.is_pressed and game_option == 1:
            game_option = 1
            time.sleep(0.3)
        elif button_1.is_pressed and game_option == 2:
            game_option = 1
            time.sleep(0.3)
        elif button_1.is_pressed and game_option == 3:
            game_option = 2
            time.sleep(0.3)
        elif button_2.is_pressed and game_option == 1:
            game_option = 2
        elif button_2.is_pressed and game_option == 2:
            game_option = 3
            time.sleep(0.3)
        elif button_1.is_pressed and game_option == 3:
            game_option = 3
            time.sleep(0.3)

        game_select_options(game_option)

        if button_4.is_pressed and game_option == 3:
            game_loop()
            time.sleep(0.3)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    gameExit = False
    option = 1

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
               
        TextSurf_1, TextRect_1 = text_objects("godispong", largeText, black)
        TextRect_1.center = ((display_width / 2), (display_height) * 0.2)
        gameDisplay.blit(TextSurf_1, TextRect_1)

        if button_1.is_pressed and option == 1:
            option = 1
            time.sleep(0.3)
        elif button_1.is_pressed and option == 2:
            option = 1
            time.sleep(0.3)
        elif button_1.is_pressed and option == 3:
            option = 2
            time.sleep(0.3)
        elif button_2.is_pressed and option == 1:
            option = 2
            time.sleep(0.3)
        elif button_2.is_pressed and option == 2:
            option = 3
            time.sleep(0.3)
        elif button_2.is_pressed and option == 3:
            option = 3
            time.sleep(0.3)

        if button_3.is_pressed and option == 1:
            game_select()
            time.sleep(0.3)

        start_menu_options(option)

        pygame.display.update()
        clock.tick(15)

game_loop()
pygame.quit()
quit()
