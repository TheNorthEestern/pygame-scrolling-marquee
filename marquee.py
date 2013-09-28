import pygame
# Global imports are bad juju, for posterity's sake, don't do this in your code
from pygame.locals import *
from sys import exit

# Specify display dimensions and filenames
SCREEN_SIZE = (640, 480)
scrolling_image_filename = 'img/r_dogs2.png'
stationary_image_filename = 'img/flames.gif'

# Reads like English, if none of this makes sense, ping me :D
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
background = pygame.image.load(stationary_image_filename).convert()
foreground = pygame.image.load(scrolling_image_filename).convert_alpha()

x, y = 0, 0
move_x = 0

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -5
            elif event.key == K_RIGHT:
                move_x = +5

        if event.type == KEYUP:
            if event.key == K_LEFT:
                move_x = 0 
            elif event.key == K_RIGHT:
                move_x = 0

    x += move_x

    screen.fill((0, 0, 0))
    screen.blit(background, (0, y))
    screen.blit(foreground, (x, y))

    pygame.display.update()
