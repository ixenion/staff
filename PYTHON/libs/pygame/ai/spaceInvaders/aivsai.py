
import pygame
import os
import sys
import time
import random
import neat
import tkinter as tk
import pickle
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

gen1 = 0
gen2 = 0
save_init_fitness1 = save_init_fitness2 = 0.5
target_move_dirct1 = 0
target_move_dirct2 = 0
change_bot_mov_dir = False

#LOAD_MODEL = True

###################
###   classes   ###
###################

class AI:
    def __init__(self, aiImg, top):
        self.img = aiImg
        self.x = random.randint(wnd_width/240, (wnd_width-64-(wnd_width/240)))
        self.vel = 5
        if top:
            self.y = (wnd_height/7)
        else:
            self.y = (wnd_height - (wnd_height/7))

    def draw(self, ai_x, ai_y):
        self.x = ai_x
        self.y = ai_y
        win.blit(self.img, (self.x, self.y))

    def right(self):
        #print ('x before: ', self.x)
        self.x += self.vel
        #print ('x after: ', self.x)
        if self.x >= wnd_width-64-(wnd_width/240):
            self.x = wnd_width-64-(wnd_width/240)
    
    def left(self):
        self.x -= self.vel
        if self.x <= 8:
            self.x = 8

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

class Bullet:
    #direction = "1" for top ai and "-1" for bottom ai
    def __init__(self, blImg, direction, vel, ship):
        self.img = blImg
        self.vel = direction * vel
        self.ready = True
        if not hasattr(self, 'x'):
            self.x = ship.x
            self.y = ship.y

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

def run(config_file):
    """
    runs the NEAT algorithm to train a neural network.
    :param config_file: location of config file
    :return: None
    """
    # for top ai (config1)
    config1 = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)
    # for bottom ai (config2)
    config2 = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)


    # Create the population, which is the top-level object for a NEAT run.
    # ai1
    p1 = neat.Population(config1)
    # ai2
    p2 = neat.Population(config2)

    # Add a stdout reporter to show progress in the terminal.
    # ai1
    p1.add_reporter(neat.StdOutReporter(True))
    stats1 = neat.StatisticsReporter()
    p1.add_reporter(stats1)
    #p.add_reporter(neat.Checkpointer(5))
    # ai2
    #p2.add_reporter(neat.StdOutReporter(True))
    #stats2 = neat.StatisticsReporter()
    #p2.add_reporter(stats2)

    # Run for up to 50000 generations.
    # ai1
    winner = p1.run(eval_genomes, 50000)

    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))

#pygame.init()

def eval_genomes(genomes, config):

    global saveTime, win, gen1, gen2, save_init_fitness1, save_init_fitness2,  target_move_dirct1, target_move_dirct2, change_bot_mov_dir
    window = win

    # ai1
    nets1 = []
    ais1 = []
    ge1 = []
    ai1buls = []
    gen1 += 1
    mvdrct1 = []
    # ai2
    nets2 = []
    ais2 = []
    ge2 = []
    ai2buls = []
    gen2 += 1
    mvdrct2 = []

    
    # ships img
    ai2Img = pygame.image.load(os.path.join("imgs", "satellite64.png"))
    ai2score = 0

    ai1Img = pygame.image.load(os.path.join("imgs", "aiship64.png"))
    ai1Img = pygame.transform.flip(ai1Img, False, True)
    #ai = AI(aiImg)
    ai1score = 0

    # bullets img
    ai2blImg = pygame.image.load(os.path.join("imgs", "bullet32-1.png"))
    #ai2bul = Bullet(ai2blImg, -1, 4)
    ai1blImg = pygame.image.load(os.path.join("imgs", "bullet32-2.png"))
    ai1blImg = pygame.transform.flip(ai1blImg, False, True)

    for genome_id, genome in genomes:
        genome.fitness = 0.0
        # ai1
        net = neat.nn.RecurrentNetwork.create(genome, config)
        nets1.append(net)
        ai1 = AI(ai1Img, 1)     # AI(img, top) if top=1 - place at top
        ais1.append(ai1)
        ai1bul = Bullet(ai1blImg, 1, 10, ai1)     # Bullet(img, direction, speed)
        ai1buls.append(ai1bul)
        ge1.append(genome)
        mvdrct1.append(target_move_dirct1)
        # ai2
        #net = neat.nn.FeedForwardNetwork.create(genome, config)
        with open("./pickles2/bestOfTheBestTop.pickle", "rb") as f:
            net = pickle.load(f)
        nets2.append(net)
        ai2 = AI(ai2Img, 0)
        ais2.append(ai2)
        ai2bul = Bullet(ai2blImg, -1, 10, ai2)
        ai2buls.append(ai2bul)
        ge2.append(genome)
        mvdrct2.append(target_move_dirct2)
        #nets[ge.index(genome)].activate((input1, input2, input3, input4, input5, input6, input7, hidden1, hidden2))

    clock = pygame.time.Clock()
    eventtype = ''
    run = True
    
    startTime = time.time()
    currTime = 0
    #frame = 0

    while run and (len(ais1) > 0 and len(ais2) > 0):
        
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
        
#################################################################################################

        aiszip = zip(ais1, ais2)

#########################################################################################################

        # ai1 & ai2 movement
        for xx, aizip in enumerate(aiszip):
            ai1 = aizip[0]
            ai2 = aizip[1]
            #ge2[ais2.index(ai2)].fitness += 0.0001
            bodydx = ai1.x - ai2.x #distance betw ai1 and ai2
            bodydy = ai1.y - ai2.y
            bullt1dx = ai2buls[xx].x - ai1.x
            bullt1dy = ai2buls[xx].y - ai1.y
            #output = nets[ais.index(ai)].activate((p1bul.x, p1bul.y, player1.x, player1.y, ai.x, ai.y))
            #output1 = nets1[ais1.index(ai1)].activate((mvdrct2[xx], bodydx, bodydy, bullt1dx, bullt1dy, ai1.x, ai1.y))
            output1 = nets1[ais1.index(ai1)].activate((mvdrct2[xx], bodydx, bodydy, bullt1dx, bullt1dy))
            
            bullt2dx = ai2.x - ai1buls[xx].x
            bullt2dy = ai2.y - ai1buls[xx].y
            #output2 = nets2[ais2.index(ai2)].activate((mvdrct1[xx], bodydx, bodydy, bullt2dx, bullt2dy, ai2.x, ai2.y))
            output2 = nets2[ais2.index(ai2)].activate((mvdrct1[xx],(bodydx), (bodydy), bullt2dx, bullt2dy))

            #i = output.index(max(output))
            
            # AI1
            # ai1 move right
            if output1[0] > 0.5:
                ai1.right()
                mvdrct1[xx] = 1
                #ge[xx].fitness += 0.0002# is it correct to apreciate for output?
                #ge[xx].fitness += 0.0002
            # ai1 move left
            elif output1[0] < -0.5:
                ai1.left()
                mvdrct1[xx] = -1
            # ai1 stay
            elif output1[0] < 0.2 and output1[0] > -0.2 :
                mvdrct1[xx] = 0
            # ai1 shot
            if output1[1] > 0.5:
                #print ('ai_r1 ', aibul.ready)
                ai1buls[xx].ready = False
                #ge[xx].fitness += 0.0001
            #if output[0] > 0.5 and output[1] > 0.5:
            #    print ("turn left and right simultanuously ;)")
            
            # AI2
            # ai2 move right
            if output2[0] > 0.5:
                ai2.right()
                mvdrct2[xx] = 1
                #ge[xx].fitness += 0.0002# is it correct to apreciate for output?
                #ge[xx].fitness += 0.0002
            # ai2 move left
            elif output2[0] < -0.5:
                ai2.left()
                mvdrct2[xx] = -1
            # ai2 stay
            elif output2[0] < 0.2 and output2[0] > -0.2 :
                mvdrct2[xx] = 0
            # ai2 shot
            if output2[1] > 0.5:
                #print ('ai_r1 ', aibul.ready)
                #ai2buls[xx].ready = False
                pass
            
##############################################################################

            
            # Score at ship's corner
            # AI1
            score_label1 = fit_font.render(str(round(ge1[xx].fitness)),1,(0,0,0))
            win.blit(score_label1, (ai1.x, ai1.y - 32))
            
            ai1.draw(ai1.x, ai1.y)
            ai1buls[xx].draw(ai1.x+16, ai1.y-16)
            
            # AI2
            score_label2 = fit_font.render(str(round(ge2[xx].fitness)),1,(0,0,0))
            win.blit(score_label2, (ai2.x, ai2.y - 32))

            ai2.draw(ai2.x, ai2.y)
            ai2buls[xx].draw(ai2.x+16, ai2.y-16)
            
        # collide
        # print("aiszip", aiszip)
        # for xx, aizip in enumerate(aiszip):
            #ai1 = aizip[0]
            #ai2 = aizip[1]
            '''
            # AI2
            if collide(ai1, ai2buls[xx], ai2):           # (target, bullet, shoter)
                ai2buls[xx].y = ai2.y + 16   
                ai2score += 1
                ge2[ais2.index(ai2)].fitness += 0.5 # add score to ai2
                ge1[ais1.index(ai1)].fitness -= 0.55
                #nets.pop(ais.index(ai))
                #ge.pop(ais.index(ai))
                #ais.pop(ais.index(ai))
            '''
            # AI1
            if collide(ai2, ai1buls[xx], ai1):
                ai1buls[xx].y = ai1.y - 16
                ai1score += 1
                ge1[ais1.index(ai1)].fitness += 0.5
                #ge2[ais2.index(ai2)].fitness -= 0.2
                
                #nets2.pop(ais2.index(ai2))
                #ge2.pop(ais2.index(ai2))
                #ais2.pop(ais2.index(ai2))
            #ge2[ais2.index(ai2)].fitness += 0.0001
            
            
        
        #frame += 1
        
        deltTime = time.time() - startTime
        # save max fitness genome
        # every 60 seconds (60x2 frame)
        if deltTime > saveTime:
            startTime = time.time()
            
            # determine best
            # save the best

            fitarray = []
            for xx, ai1 in enumerate(ais1):
                fitarray.append([xx, ge1[ais1.index(ai1)].fitness])
            sortedfit = quick_sort(fitarray)                        # [0][0] - maxfit index, [last][0] - minfit index
            try:
                maxfit1 = sortedfit[0][1]
            except IndexError:
                maxfit1 = 0
                pass
            if maxfit1 >= save_init_fitness1:
                pickle.dump(nets1[sortedfit[0][0]],open("./pickles2/bestOfTheBestTop.pickle", "wb"))
                save_init_fitness1 = maxfit1
            #rotate(sortedfit, -1)                                   # now [0][0] - minfit index, [last][0] - maxfit index
            ais1.pop(sortedfit[len(sortedfit)-1][0])
            nets1.pop(sortedfit[len(sortedfit)-1][0])
            ge1.pop(sortedfit[len(sortedfit)-1][0])

            '''
            if maxfit2 >= save_init_fitness2:
                print("Saving BestOfTheBest 2 ", maxfit2)
                pickle.dump(nets2[0],open("./pickles2/bestOfTheBestBot.pickle", "wb"))
                save_init_fitness2 = maxfit2
           '''

            '''
            # kill worst
            # AI 1
            try:
                print("deleting1 ", minge1)
                #nets1.pop(minge1)
                #ge1.pop(minge1)
                ais1.pop(minge1)
                
                # AI 2
                print("deleting2 ", minge2)
                nets2.pop(minge2)
                ge2.pop(minge2)
                
                ais2.pop(minge2)
                
            except UnboundLocalError:
                minge1 = 0
                pass
            except IndexError:
                minge1 -=1
        '''

        #print lable
        # AI 1
        # generations
        score_label = stat_font.render("Gens1: " + str(gen1),1,(0,0,0))
        win.blit(score_label, (10, 170))
        # alive
        score_label = stat_font.render("Alive1: " + str(len(ais1)),1,(0,0,0))
        win.blit(score_label, (10, 220))

        score_label = stat_font.render("AI1save: " + str(save_init_fitness1),1,(0,0,0))
        win.blit(score_label, (740, 220))

        # AI 2
        # generations
        score_label = stat_font.render("Gens2: " + str(gen1),1,(0,0,0))
        win.blit(score_label, (10, 390))
        # alive
        score_label = stat_font.render("Alive2: " + str(len(ais1)),1,(0,0,0))
        win.blit(score_label, (10, 440))
        
        score_label = stat_font.render("AI2save: " + str(save_init_fitness2),1,(0,0,0))
        win.blit(score_label, (740, 440))
        '''
        score_label = stat_font.render("AI: " + str(ai1score),1,(0,0,0))
        win.blit(score_label, (780, 550))
        '''
        
        score_label = stat_font.render("AI1drct: " + str(mvdrct1[0]),1,(0,0,0))
        win.blit(score_label, (390, 550))
        
        
        try:
            score_label = stat_font.render("AI1Max: " + str(maxfit1),1,(0,0,0))
            win.blit(score_label, (740, 170))
            #score_label = stat_font.render("AI2Max: " + str(maxfit2),1,(0,0,0))
            #win.blit(score_label, (740, 390))
        except UnboundLocalError:
            pass
        except IndexError:
            pass
        

        # update display
        pygame.display.update()



if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)
