
import pygame
import os
import time
import random
import neat
import tkinter as tk


# to get rid of "ALSA underrun ocured"
os.environ['SDL_AUDIODRIVER'] = 'dsp'

pygame.font.init()

# get screen width
window = tk.Tk()
sw = window.winfo_screenwidth()
sh = window.winfo_screenheight()

#####################
###   constants   ###
#####################

# title
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(os.path.join("imgs", "alien2-32.png"))
pygame.display.set_icon(icon)

wnd_width = sw/2
wnd_height = sh/2
stat_font = pygame.font.SysFont("comicsans", 50)
win = pygame.display.set_mode((int(wnd_width), int(wnd_height)))


###################
###   classes   ###
###################

class Player:
    def __init__(self, plrImg):
        self.img = plrImg
        self.x = random.randint(wnd_width/240, (wnd_width-64-(wnd_width/240)))
        self.y = (wnd_height - (wnd_height/7))
        self.vel = 3

    def draw(self, plr_x, plr_y):
        self.x = plr_x
        self.y = plr_y
        win.blit(self.img, (self.x, self.y))
    
    def move(self, eventtype):
        if eventtype == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #print ("left!")
                self.x += -self.vel
                if self.x <= 8:
                    self.x = 8
            if event.key == pygame.K_RIGHT:
                #print ("right!")
                self.x += self.vel
                if self.x >= wnd_width-64-(wnd_width/240):
                    self.x = wnd_width-64-(wnd_width/240)
            if event.key == pygame.K_UP:
                #print ("up!")
                self.y += -self.vel
                if self.y <= wnd_height - (wnd_height/3):
                    self.y = wnd_height - (wnd_height/3)
            if event.key == pygame.K_DOWN:
                #print ("down!")
                self.y += self.vel
                if self.y >= wnd_height - (wnd_height/7):
                    self.y = wnd_height - (wnd_height/7)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
            

class AI:
    def __init__(self, aiImg):
        self.img = aiImg
        self.x = random.randint(wnd_width/240, (wnd_width-64-(wnd_width/240)))
        self.y = (wnd_height/7)
        self.vel = 3

    def draw(self, ai_x, ai_y):
        self.x = ai_x
        self.y = ai_y
        win.blit(self.img, (self.x, self.y))

    def move(self, eventtype, shoter_x):
        pass

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

class Bullet:
    #direction = "1" for enemy and "-1" for player
    def __init__(self, blImg, direction, vel):
        self.img = blImg
        self.vel = direction * vel
        self.ready = True

    def draw(self, shoter_x, shoter_y):
        if not hasattr(self, 'y'):
            self.x = shoter_x
            self.y = shoter_y
        if self.ready:
            self.x = shoter_x
            self.y = shoter_y
        if self.vel < 0 and self.y < 0:
            self.ready = True
            self.x = shoter_x
            self.y = shoter_y
        if self.vel > 0 and self.y > wnd_height:
            self.ready = True
            self.x = shoter_x
            self.y = shoter_y
        if not self.ready:
            win.blit(self.img, (self.x, self.y))
            self.y += self.vel
            
    def shot(self, eventtype):
        if eventtype == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.ready:
                    self.ready = False
    
    def get_mask(self):
        return pygame.mask.from_surface(self.img)
    
class Collide:
    def __init__(self, targetA, bulletB):
        self.a = targetA
        self.b = bulletB

#####################
###   functions   ###
#####################

def collide(targetA, bulletB, targetB):
    targetA_mask = targetA.get_mask()
    bulletB_mask = bulletB.get_mask()
    offset = (round(targetA.x - bulletB.x), round(targetA.y - bulletB.y))
    touch = bulletB_mask.overlap(targetA_mask, offset)
    
    if touch:
        bulletB.ready = True
        bulletB.x = targetB.x+16
        #bulletB.y = targetB.y
        return True
    else:
        return False

def print_score(first, second):
    print("\rplayer: ", first, "\nai: ", second)

################
###   main   ###
################

pygame.init()

plrImg1 = pygame.image.load(os.path.join("imgs", "spaceship64.png"))
player1 = Player(plrImg1)
p1score = 0

aiImg = pygame.image.load(os.path.join("imgs", "aiship64.png"))
aiImg = pygame.transform.flip(aiImg, False, True)
ai = AI(aiImg)
aiscore = 0

p1blImg = pygame.image.load(os.path.join("imgs", "bullet32-1.png"))
p1bul = Bullet(p1blImg, -1, 10)

aiblImg = pygame.image.load(os.path.join("imgs", "bullet32-2.png"))
aiblImg = pygame.transform.flip(aiblImg, False, True)
aibul = Bullet(aiblImg, 1, 10)

clock = pygame.time.Clock()

eventtype = ''
run = True
while run:
    clock.tick(60)
    win.fill((255,255,255))

    for event in pygame.event.get():
        eventtype = event.type
        if event.type == pygame.QUIT:
            run = False
            quit()
            break

    # player1 key movement
    player1.move(eventtype)
    
    # debug
    if eventtype == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #print ("key released")
            pass
    
    # draw objects
    player1.draw(player1.x, player1.y)
    ai.draw(ai.x, ai.y)

    # pilot1 shot
    # manual shot
    p1bul.shot(eventtype)
    # auto shot
    #p1bul.ready = False
    # draw bullet
    p1bul.draw(player1.x+16, player1.y+16)
    
    #ai shot
    #aibul.ready = False
    aibul.draw(ai.x+16, ai.y-16)
    
    # collide
    if collide(ai, p1bul, player1):
        p1bul.y = player1.y + 16
        p1score += 1
        print_score(p1score, aiscore)
    if collide(player1, aibul, ai):
        aibul.y = ai.y - 16
        aiscore += 1
        print_score(p1score, aiscore)
    
    # update display
    pygame.display.update()

