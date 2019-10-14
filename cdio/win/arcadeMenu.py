import pygame
import time
import random

pygame.init()

coin_sound = pygame.mixer.Sound("coin.wav") #load sound
pygame.mixer.music.load("level_1.wav") #load music

display_width = 800
display_height = 480

#define colours (R, G, B)
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
thing_colour = (250, 112, 150) #cdio

red = (200, 0, 0)
bright_red = (255, 0, 0)

green = (0, 200, 0)
bright_green = (0, 255, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('GodisPong')

#game clock
clock = pygame.time.Clock()

#load image
flamingoImg = pygame.image.load('flamingo.png')

flamingo_width = 200

pause = False
#crash = True

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render('Dodged: ' + str(count), True, black)
    gameDisplay.blit(text, (0, 0))

#scale image
#flamingoImg = pygame.transform.scale(flamingoImg, (100, 160))

def things(thing_x, thing_y, thing_w, thing_h, colour):
    pygame.draw.rect(gameDisplay, colour, [thing_x, thing_y, thing_w, thing_h])    

#display image given a position
def flamingo(x, y):
    gameDisplay.blit(flamingoImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('karmatic_arcade.ttf', 80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height * 0.3))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    #message_display('you crashed')

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(coin_sound)
    
    #gameDisplay.fill(white)
    largeText = pygame.font.Font('karmatic_arcade.ttf', 80)
    TextSurf, TextRect = text_objects("You crashed", largeText)
    TextRect.center = ((display_width / 2), (display_height * 0.3))
    gameDisplay.blit(TextSurf, TextRect)
    
    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play again", 150, 300, 100, 50, green, bright_green, game_loop)
        button("QUIT", 450, 300, 100, 50, red, bright_red, quitgame)
              
        pygame.display.update()
        clock.tick(15)  

def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    #print(mouse)

    click = pygame.mouse.get_pressed()
    #print(click)
    
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
            
##            if action == "play":
##                game_loop()
##            elif action == "quit":
##                pygame.quit()
##                quit()
            
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("karmatic_arcade.ttf", 30)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    
def paused():

    pygame.mixer.music.pause()

    #gameDisplay.fill(white)
    largeText = pygame.font.Font('karmatic_arcade.ttf', 80)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2), (display_height * 0.3))
    gameDisplay.blit(TextSurf, TextRect)
    
    while pause:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", 150, 300, 100, 50, green, bright_green, unpause)
        button("QUIT", 450, 300, 100, 50, red, bright_red, quitgame)
              
        pygame.display.update()
        clock.tick(15)    
                
#runs only once
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('karmatic_arcade.ttf', 80)
        TextSurf, TextRect = text_objects("GodisPong", largeText)
        TextRect.center = ((display_width / 2), (display_height * 0.3))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 150, 300, 100, 50, green, bright_green, game_loop)
        button("QUIT", 450, 300, 100, 50, red, bright_red, quitgame)
              
        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause

    pygame.mixer.music.play(-1) #music loop forever
    
    #define image start position
    x = (display_width * 0.4)
    y = (display_height * 0.5)

    x_change = 0

    thing_start_x = random.randrange(0, display_width)
    thing_start_y = -600
    thing_speed = 3
    thing_width = 50
    thing_height = 50

    dodged = 0
    
    gameExit = False

    while not gameExit:

        #event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #gameExit = True
                pygame.quit()
                quit()
                
            #print all the user input events like key pressed or mouse clicks
            #print(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                              
        x += x_change

        #background colour
        gameDisplay.fill(white)

        #things(thing_x, thing_y, thing_w, thing_h, colour)
        things(thing_start_x, thing_start_y, thing_width, thing_height, thing_colour)
        thing_start_y += thing_speed

        #display image
        flamingo(x, y)

        #draw score last
        things_dodged(dodged)

        #define boundaries
        if x > display_width - flamingo_width or x < 0:
            #gameExit = True
            crash()

        #when objects dissapear of the screen
        if thing_start_y > display_height:
            thing_start_y = 0 - thing_height
            thing_start_x = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)
            

        #crash
        if y < thing_start_y + thing_height:
            print('y crossover')
            if x > thing_start_x and x < thing_start_x + thing_width or x + flamingo_width > thing_start_x and x + flamingo_width < thing_start_x + thing_width:
                print('x crossover')
                crash()
        
        #update can take a parameter, which is the only thing that gets updated
        #update without parameters updates the whole frame
        #flip updates the whole frame
        pygame.display.update()

        #fps
        clock.tick(60)
        
game_intro()
game_loop()
pygame.quit()
quit()
