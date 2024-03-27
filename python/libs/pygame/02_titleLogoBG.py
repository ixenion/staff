# change title, logo, background img
import pygame
import os

os.environ['SDL_AUDIODRIVER'] = 'dsp'# to get rid of "ALSA underrun ocured"
# initialise the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption('Space Invaders')# not working(?)
#icon = pygame.image.load('./imgs/ufo.png')#pops at top left win corner
#pygame.display.set_ion(icon)

# game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # rgb palit BG
    screen.fill((0,255,255))
    pygame.display.update()
