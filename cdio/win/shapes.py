import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((800, 480))
gameDisplay.fill(black)

#pixel: define array, pixel coordinate
pixelArray = pygame.PixelArray(gameDisplay)
pixelArray[10][20] = green

#line: start point, end point, thickness
pygame.draw.line(gameDisplay, blue, (100, 200), (300, 450), 5)

#rectangle: upper right corner, width, height
pygame.draw.rect(gameDisplay, red, (400, 400, 50, 25))

#circle: center point, radius
pygame.draw.circle(gameDisplay, white, (300, 150), 76)

#polygon: vertices
pygame.draw.polygon(gameDisplay, green, ((25, 75), (76, 125), (250, 375), (400, 25)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
