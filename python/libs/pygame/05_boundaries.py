# change title, logo, background img
import pygame
import os

os.environ['SDL_AUDIODRIVER'] = 'dsp'# to get rid of "ALSA underrun ocured"
# initialise the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('./imgs/alien32.png')#pops at top left win corner
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('./imgs/spaceship64.png')
playerX = 370
playerY = 480
playerX_ch = 0


def player(x, y):
    # to draw playeer img on win
    screen.blit(playerImg, (x, y))

# game loop
run = True
while run:
    
    # rgb palit BG
    screen.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # keystrokes
    # if keystroke is pressed check whether its right or left
    if event.type == pygame.KEYDOWN:
        print("a keystroke is pressed")
        if event.key == pygame.K_LEFT:
            print("left arrow is pressed")
            playerX_ch = -0.7
        if event.key == pygame.K_RIGHT:
            print("right arrow is pressed")
            playerX_ch = 0.7

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key != pygame.K_RIGHT:
            print("keystroke has been released")
            playerX_ch = 0

    
    # key strokes
    playerX += playerX_ch
    
    # boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY)
    pygame.display.update()

