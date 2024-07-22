
import pygame
import os
import time
import random
import neat
import tkinter as tk
import pickle
import sys
from math import cos
from math import pi
#from plumbum.cmd import echo
#import subprocess 

try:
    saveTime = 6/int(sys.argv[1])
    clocktick = 60*int(sys.argv[1])
except IndexError:
    saveTime = 6
    clocktick = 60

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
fit_font = pygame.font.SysFont("comicsans", 35)
win = pygame.display.set_mode((int(wnd_width), int(wnd_height)))

gen = 0
save_init_fitness = -2
target_move_dirct = 0
change_bot_mov_dir = False

#LOAD_MODEL = True

###################
###   classes   ###
###################

class Player:
    
    global target_move_dirct

    def __init__(self, plrImg):
        self.img = plrImg
        self.x = random.randint(wnd_width/240, (wnd_width-64-(wnd_width/240)))
        self.y = (wnd_height - (wnd_height/7))
        #self.y = random.randint((wnd_height - (wnd_height/4)), (wnd_height - (wnd_height/7)))
        self.vel = 3

    def draw(self, plr_x, plr_y):
        self.x = plr_x
        self.y = plr_y
        win.blit(self.img, (self.x, self.y))
    
    def move(self, event):
        #for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x += -self.vel
                target_move_dirct = -1
                if self.x <= 8:
                    self.x = 8
            if event.key == pygame.K_RIGHT:
                self.x += self.vel
                target_move_dirct = 1
                if self.x >= wnd_width-64-(wnd_width/240):
                    self.x = wnd_width-64-(wnd_width/240)
            if event.key == pygame.K_UP:
                self.y += -self.vel
                if self.y <= wnd_height - (wnd_height/3):
                    self.y = wnd_height - (wnd_height/3)
            if event.key == pygame.K_DOWN:
                self.y += self.vel
                if self.y >= wnd_height - (wnd_height/7):
                    self.y = wnd_height - (wnd_height/7)

    def right(self):
        self.x += self.vel
        if self.x >= wnd_width-(64+64)-(wnd_width/240):
            self.x = wnd_width-(64+64)-(wnd_width/240)
    def left(self):
        self.x -= self.vel
        if self.x <= (8+64):
            self.x = (8+64)
    
    def get_mask(self):
        return pygame.mask.from_surface(self.img)
            

class AI:
    def __init__(self, aiImg):
        self.img = aiImg
        self.x = random.randint(wnd_width/240, (wnd_width-64-(wnd_width/240)))
        self.y = (wnd_height/7)
        self.vel = 5

    def draw(self, ai_x, ai_y):
        self.x = ai_x
        self.y = ai_y
        win.blit(self.img, (self.x, self.y))

    def right(self):
        #print ('x before: ', self.x)
        self.x += self.vel
        #print ('x after: ', self.x)
        if self.x >= wnd_width-64-(wnd_width/240):     # 128 - 64+64
            self.x = wnd_width-64-(wnd_width/240)
    
    def left(self):
        self.x -= self.vel
        if self.x <= 8:     # 8+64
            self.x = 8

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

class Bullet:
    #direction = "1" for enemy and "-1" for player
    def __init__(self, blImg, direction, vel, shoter_x, shoter_y):
        self.img = blImg
        self.vel = direction * vel
        self.ready = True
        if not hasattr(self, 'y') or not hasattr(self, 'x'):
            self.x = shoter_x
            self.y = shoter_y

    def draw(self, shoter_x, shoter_y):
        if not hasattr(self, 'y') or not hasattr(self, 'x'):
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
            
    def shot(self, event):
        #for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.ready:
                    self.ready = False
    
    def get_mask(self):
        return pygame.mask.from_surface(self.img)


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

def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
        
    items_greater = []
    items_lower = []
    
    for item in sequence:
        if item[1] > pivot[1]:
            items_greater.append(item)
        else:
            items_lower.append(item)
            
    return quick_sort(items_greater) + [pivot] + quick_sort(items_lower)

def rotate(List, n):
    return List[n:] + List[:n]


def run(config_file):
    """
    runs the NEAT algorithm to train a neural network.
    :param config_file: location of config file
    :return: None
    """
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    #p.add_reporter(neat.Checkpointer(5))

    # Run for up to 50 generations.
    winner = p.run(eval_genomes, 50000)

    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))

#pygame.init()

def eval_genomes(genomes, config):

    global win, gen, save_init_fitness, target_move_dirct, change_bot_mov_dir
    window = win
    display_mode = 0

    nets = []
    ais = []
    ge = []
    aibuls = []
    gen += 1
    aibulcntrs = []
    
    bot1Img = pygame.image.load(os.path.join("imgs", "satellite64.png"))
    bot1 = Player(bot1Img)
    b1score = 0

    aiImg = pygame.image.load(os.path.join("imgs", "aiship64.png"))
    aiImg = pygame.transform.flip(aiImg, False, True)
    #ai = AI(aiImg)
    aiscore = 0

    bblImg = pygame.image.load(os.path.join("imgs", "bullet32-1.png"))
    b1bul = Bullet(bblImg, -1, 4, bot1.x+16, bot1.y+16)
    b1bulready = True

    # ai bul img
    aiblImg = pygame.image.load(os.path.join("imgs", "bullet32-2.png"))
    aiblImg = pygame.transform.flip(aiblImg, False, True)
    # ai contr bul img
    aibulcntrImg = pygame.image.load(os.path.join("imgs", "bullet32-1.png"))




    for genome_id, genome in genomes:
        genome.fitness = 0.0
        #net = neat.nn.FeedForwardNetwork.create(genome, config)
        net = neat.nn.RecurrentNetwork.create(genome, config)
        #with open("./pickles/Score6.pickle", "rb") as f:
        #    net = pickle.load(f)
        nets.append(net)
        ai = AI(aiImg)
        ais.append(ai)
        aibul = Bullet(aiblImg, 1, 10, ai.x+16, ai.y-16)
        aibuls.append(aibul)
        ge.append(genome)
        aibulcntr = Bullet(aibulcntrImg, -1, 7, ai.x+16, bot1.y+16)
        aibulcntrs.append(aibulcntr)
        #nets[ge.index(genome)].activate((input1, input2, input3, input4, input5, input6, input7, hidden1, hidden2))

    clock = pygame.time.Clock()
    eventtype = ''
    run = True
    #frame = 0
    startTime = time.time()
    while run and len(ais) > 0 :
        
        clock.tick(clocktick)
        win.fill((255,255,255))

        for event in pygame.event.get():
            #print ("evkey: ", event)
            eventtype = event.type
            event1 = event
            if event.type == pygame.QUIT:
                run = False
                quit()
                break
        
                # player1 key movement
        ###################
        ###   bot   ###
        ###################
        try:
            bot1.move(event)
        except UnboundLocalError:
            pass
        try:
            b1bul.shot(event)
        except UnboundLocalError:
            pass
        
        # BOT MAIN
        # bot movement
        try:
            if bot1.x <= 72 or bot1.x >= wnd_width-(64+64)-(wnd_width/240):
                watchto = random.randrange(len(ais))
                minm = 0
            
            if minm == 1000:
                watchto = random.randrange(len(ais))
                minm = 0
                #for xx, ai in enumerate(ais):
                    #if abs(bot1.x - ai.x) < minm:
                    #    minm = abs(bot1.x - ai.x)
                    #    watchto = xx
            try:
                minm = abs(bot1.x - ais[watchto].x)
                #print ("min: ", minm)
                #print ("watch: ", watchto)
                oldx = bot1.x
                # approach
                if (bot1.x - ais[watchto].x) >= 30:
                    bot1.left()
                    target_move_dirct = -1
                if (bot1.x - ais[watchto].x) < 30:
                    bot1.right()
                    target_move_dirct = 1
                if abs(bot1.x - ais[watchto].x) <= 32:
                    b1bul.ready = False
                    #minm = 1000
                if oldx == bot1.x:
                    target_move_dirct = 0
                #print ("target_move_dirct: ",target_move_dirct)

                pass
            except IndexError:
                minm = 1000
                pass

        except UnboundLocalError:
            minm = 1000
            pass
        
        '''# random movement
        probb = random.randrange(2)
        if probb > 1.7:
            changeDir = True
            pass
        if changeDir and target_move_dirct == -1:
            pass'''



        bot1.draw(bot1.x, bot1.y)
        b1bul.draw(bot1.x+16, bot1.y+16)

        if eventtype == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                #print ("key released")
                pass
        
        # player draw
        #player1.draw(player1.x, player1.y)
        
        # pilot1 shot
        # manual shot
        #p1bul.shot(eventtype)
        # auto shot
        #p1bul.ready = False
        # draw bullet
        #p1bul.draw(player1.x+16, player1.y+16)
        
        for xx, ai in enumerate(ais):
            
            # aibulcntr staff
            if aibulcntrs[xx].ready: #and not b1bulready:
                aibulcntrs[xx].ready = False

            #pdx = ai.x - bot1.x #distance betw player and ai
            
            #bdx = aibulcntrs[xx].x - ai.x
            #bdy = aibulcntrs[xx].y - ai.y

            # normalization
            aicntrbxnorm = aibulcntrs[xx].x / wnd_width
            aicntrbynorm = aibulcntrs[xx].y / wnd_width
            axnorm = ai.x / wnd_width
            aynorm = ai.y / wnd_height
            bot1xnorm = bot1.x / wnd_width
            bot1ynorm = bot1.y / wnd_height
            #pdx = pdx/wnd_width

            #output = nets[ais.index(ai)].activate((p1bul.x, p1bul.y, player1.x, player1.y, ai.x, ai.y))
            #output = nets[ais.index(ai)].activate((target_move_dirct, pdx, pdy, bdx, bdy, ai.x, ai.y))
            #output = nets[ais.index(ai)].activate((target_move_dirct, pdx, bdx, bdy))
            output = nets[ais.index(ai)].activate((axnorm, aynorm, aicntrbxnorm, aicntrbynorm, bot1xnorm, bot1ynorm))
            
            #i = output.index(max(output))
            if output[0] > 0.3:
                ai.right()
                #ge[xx].fitness += 0.0002# is it correct to apreciate for output?
                #ge[xx].fitness += 0.0002
            elif output[0] < -0.3:
                ai.left()
            if output[1] > 0.3:
                #print ('ai_r1 ', aibul.ready)
                aibuls[xx].ready = False
                #ge[xx].fitness += 0.0001
            #if output[0] > 0.5 and output[1] > 0.5:
            #    print ("turn left and right simultanuously ;)")
            
            '''
            # revards and penalties
            if abs(bot1.x - ai.x) <= 64:
                ge[xx].fitness += 0.001
                pass
            
            if ai.x <= 72 or ai.x >= wnd_width-(64+64)-(wnd_width/240):
                ge[xx].fitness -= 0.002
                #nets.pop(xx)
                #ge.pop(xx)
                #ais.pop(xx)
            '''
            score_label = fit_font.render(str(round(ge[xx].fitness)),1,(0,0,0))
            win.blit(score_label, (ai.x, ai.y - 32))
            
            ai.draw(ai.x, ai.y)
            aibuls[xx].draw(ai.x+16, ai.y-16)
            aibulcntrs[xx].draw(ai.x+16, bot1.y+16)
        
        # collide
        for xx, ai in enumerate(ais):
            '''
            if collide(ai, b1bul, bot1):
                b1bul.y = bot1.y + 16
                b1score += 1
                ge[ais.index(ai)].fitness -= 2.0
                #nets.pop(ais.index(ai))
                #ge.pop(ais.index(ai))
                ais.pop(ais.index(ai))
            '''
            if collide(ai, aibulcntrs[xx], bot1):
                aibulcntrs[xx].y = bot1.y + 16
                b1score += 1
                #ge[ais.index(ai)].fitness -= 2.0
                nets.pop(ais.index(ai))
                ge.pop(ais.index(ai))
                ais.pop(ais.index(ai))
                minm = 1000
            try:
                if collide(bot1, aibuls[xx], ais[xx]):
                    aibuls[xx].y = ai.y - 16
                    aiscore += 0.5
                    #ge[ais.index(ai)].fitness += 0.5
            except IndexError:
                print ("index error")
                pass
            except ValueError:
                print("value error")
                pass
        
        # save maxfit and kill minfit
        deltTime = time.time() - startTime
        if deltTime > saveTime:
            startTime = time.time()
            #fitarray = [[0 for x in range(1)]]
            fitarray = []
            for xx, ai in enumerate(ais):
                fitarray.append([xx, ge[ais.index(ai)].fitness])
            sortedfit = quick_sort(fitarray)                        # [0][0] - maxfit index, [last][0] - minfit index
            try:
                maxfit = sortedfit[0][1]
            except IndexError:
                maxfit = 0
                pass
            if maxfit >= save_init_fitness:
                pickle.dump(nets[sortedfit[0][0]],open("best.pickle", "wb"))
                save_init_fitness = maxfit
            #rotate(sortedfit, -1)                                   # now [0][0] - minfit index, [last][0] - maxfit index
            try:
                ais.pop(sortedfit[len(sortedfit)-1][0])
                #nets.pop(sortedfit[len(sortedfit)-1][0])
                #ge.pop(sortedfit[len(sortedfit)-1][0])
            except IndexError:
                pass

        
        # generations
        score_label = stat_font.render("Gens: " + str(gen),1,(0,0,0))
        win.blit(score_label, (10, 500))
        # alive
        score_label = stat_font.render("Alive: " + str(len(ais)),1,(0,0,0))
        win.blit(score_label, (10, 550))
        
        score_label = stat_font.render("Bot: " + str(b1score),1,(0,0,0))
        win.blit(score_label, (780, 500))

        score_label = stat_font.render("AI: " + str(aiscore),1,(0,0,0))
        win.blit(score_label, (780, 550))

        score_label = stat_font.render("Bot dir: " + str(target_move_dirct),1,(0,0,0))
        win.blit(score_label, (390, 550))

        score_label = stat_font.render("save_fit: " + str(save_init_fitness),1,(0,0,0))
        win.blit(score_label, (760, 200))
        
        try:
            score_label = stat_font.render("Max fit: " + str(maxfit),1,(0,0,0))
            win.blit(score_label, (760, 150))
        except UnboundLocalError:
            pass
        except IndexError:
            pass
        
        '''
        # update display
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    display_mode = cos(display_mode*pi/2)
        '''
        #if display_mode:
        pygame.display.update()
            

        

if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-btrainPureRN.txt')
    run(config_path)
