# change title, logo, background img
import pygame
import os
import random
import math
from pygame import mixer

os.environ['SDL_AUDIODRIVER'] = 'dsp'# to get rid of "ALSA underrun ocured"
# initialise the pygame
pygame.init()
#pygame.mixer.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
#bg = pygame.image.load('./img/bg.png')

# sound BG
#mixer.music.load('./sounds/background.wav')
#mixer.music.play(-1)# -1 means play on loop

# title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('./imgs/alien32.png')#pops at top left win corner
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('./imgs/spaceship64.png')
playerX = 370
playerY = 480
playerX_ch = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_ch = []
enemyY_ch = []
num_of_enemies = 6

for i in range(num_of_enemies):

    # game over
    if enemyY[i] > 440:
        for j in range(num_of_enemies):
            enemyY[j] = 2000
        game_over_text()
        break

    enemyImg.append(pygame.image.load('./imgs/ufo64.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_ch.append(0.3)
    enemyY_ch.append(40)

# bullet
bulletImg = pygame.image.load('./imgs/bullet32.png')
bulletX = 0
bulletY = 460
bulletX_ch = 0
bulletY_ch = 3
# ready - can't see on display, fire - can see
bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10


# game ove text
over_font = pygame.font.Font('freesansbold.ttf',64)

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def game_over_text(x, y):
    over_text = over_font.render("GAME OVER" + str(score_value), True, (255,255,255))
    screen.blit(over_text, 200, 250)


def player(x, y):
    # to draw playeer img on win
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY - bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

# game loop
run = True
while run:
    
    # rgb palit BG
    screen.fill((0,0,0))

    # BG img
    #screen.blit(bg, (0,0))#slows process
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # keystrokes
    # if keystroke is pressed check whether its right or left
    if event.type == pygame.KEYDOWN:
        #print("a keystroke is pressed")
        if event.key == pygame.K_LEFT:
            #print("left arrow is pressed")
            playerX_ch = -3
        if event.key == pygame.K_RIGHT:
            #print("right arrow is pressed")
            playerX_ch = 3
        if event.key == pygame.K_SPACE:
            print("FIRE!!!")
            if bullet_state is "ready":
                bulletX = playerX
                #bullet_Sound = mixer.Sound('./sounds/laser.wav')
                #bullet_Sound.play()
                fire_bullet(bulletX, bulletY)
                #bullet_state = "fire"

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #print("keystroke has been released")
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
    
    # enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_ch[i]
        # enemy boundaries
        if enemyX[i] <= 0:
            enemyX_ch[i] = 0.3
            enemyY[i] += enemyY_ch[i]
        elif enemyX[i] >= 736:
            enemyX_ch[i] = -0.3
            enemyY[i] += enemyY_ch[i]

        # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            #explosion_sound = mixer.Sound('./sounds/explosion.wav')
            #explosion_sound.play()
            bulletY = 460
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)


        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 460
        bullet_state = "ready"
    
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_ch
     

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()

