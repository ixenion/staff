# change title, logo, background img
import pygame
import os
import random

os.environ['SDL_AUDIODRIVER'] = 'dsp'# to get rid of "ALSA underrun ocured"
# initialise the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption('Space Invaders')
#icon = pygame.image.load('./imgs/ufo.png')#pops at top left win corner
#pygame.display.set_ion(icon)

# player
playerImg = pygame.image.load('./imgs/spaceship64.png')
playerX = 370
playerY = 480
playerX_ch = 0

# enemy
enemyImg = pygame.image.load('./imgs/ufo64.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_ch = 0.6
enemyY_ch = 40

def player(x, y):
    # to draw playeer img on win
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))

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
            playerX_ch = -0.65
        if event.key == pygame.K_RIGHT:
            print("right arrow is pressed")
            playerX_ch = 0.65

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            print("keystroke has been released")
            playerX_ch = 0

    
    # movement
    #playerX += 0.1
    
    # key strokes
    playerX += playerX_ch
    
    # player boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    enemyX += enemyX_ch
    # enemy boundaries
    if enemyX <= 0:
        enemyX_ch = 0.6
        enemyY += enemyY_ch
    elif enemyX >= 736:
        enemyX_ch = -0.6
        enemyY += enemyY_ch

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()

