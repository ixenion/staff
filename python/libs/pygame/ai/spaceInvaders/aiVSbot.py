
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

gen = 0


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
    
    def move(self, event):
        #for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x += -self.vel
                if self.x <= 8:
                    self.x = 8
            if event.key == pygame.K_RIGHT:
                self.x += self.vel
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
    def left(self):
        self.x -= self.vel
    
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
        if self.x >= wnd_width-64-(wnd_width/240):
            self.x = wnd_width-64-(wnd_width/240)
    
    def left(self):
        self.x -= self.vel
        if self.x <= 8:
            self.x = 8

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
            
    def shot(self, event):
        #for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.ready:
                    self.ready = False
    
    def get_mask(self):
        return pygame.mask.from_surface(self.img)

class event():
    def type(self):
        event = ('''<Event(1-ActiveEvent {'gain': 0, 'state': 2})>''')
        return event



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
    winner = p.run(eval_genomes, 500)

    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))

#pygame.init()

def eval_genomes(genomes, config):

    global win, gen
    window = win
    gen += 1

    nets = []
    ais = []
    ge = []
    aibuls = []

    bot1Img = pygame.image.load(os.path.join("imgs", "satellite64.png"))
    bot1 = Player(bot1Img)
    b1score = 0

    aiImg = pygame.image.load(os.path.join("imgs", "aiship64.png"))
    aiImg = pygame.transform.flip(aiImg, False, True)
    #ai = AI(aiImg)
    aiscore = 0

    bblImg = pygame.image.load(os.path.join("imgs", "bullet32-1.png"))
    b1bul = Bullet(bblImg, -1, 5)

    aiblImg = pygame.image.load(os.path.join("imgs", "bullet32-2.png"))
    aiblImg = pygame.transform.flip(aiblImg, False, True)
    
    #event = Event()

    for genome_id, genome in genomes:
        genome.fitness = 0.0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        ai = AI(aiImg)
        ais.append(ai)
        aibul = Bullet(aiblImg, 1, 10)
        aibuls.append(aibul)
        ge.append(genome)


    clock = pygame.time.Clock()
    eventtype = ''
    run = True
    while run and len(ais) > 1:
        
        clock.tick(60)
        win.fill((255,255,255))

        for event in pygame.event.get():
            #print ("evkey: ", event)
            eventtype = event.type
            event1 = event
            if event.type == pygame.QUIT:
                run = False
                quit()
                break
            #elif event.type == pygame.KEYDOWN:
            #    eventkey = event.key
            #    pass
        
                # player1 key movement
        ###################
        ###   kostul'   ###
        ###################
        try:
            bot1.move(event)
        except UnboundLocalError:
            #print ('event not defined')
            pass
                # player draw

                # pilot1 shot
                # manual shot
        try:
            b1bul.shot(event)
        except UnboundLocalError:
            #print ('event not defined')
            pass
                # auto shot
                #p1bul.ready = False
                # draw bullet
                # debug
        
        # BOT MAIN
        #print ("mindist: ", min(abs(bot1.x - ais)))
        try:
            if minm == 1000:
                for xx, ai in enumerate(ais):
                    if abs(bot1.x - ai.x) < minm:
                        minm = abs(bot1.x - ai.x)
                        watchto = xx
            try:
                minm = abs(bot1.x - ais[watchto].x)
                print ("min: ", minm)
                print ("watch: ", watchto)
                
                # approach
                if (bot1.x - ais[watchto].x) >= 30:
                    bot1.left()
                if (bot1.x - ais[watchto].x) < 30:
                    bot1.right()
                if abs(bot1.x - ais[watchto].x) <= 32:
                    b1bul.ready = False

                pass
            except IndexError:
                minm = 1000
                pass

        except UnboundLocalError:
            minm = 1000
            pass

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
            ge[xx].fitness -= 0.008
            pdx = ai.x - bot1.x #distance betw player an ai
            pdy = ai.y - bot1.y
            bdx = b1bul.x - ai.x
            bdy = b1bul.y - ai.y
            #output = nets[ais.index(ai)].activate((p1bul.x, p1bul.y, player1.x, player1.y, ai.x, ai.y))
            output = nets[ais.index(ai)].activate((pdx, pdy, bdx, bdy, ai.x, ai.y))
            
            #i = output.index(max(output))
            if output[0] > 0.5:
                ai.right()
                ge[xx].fitness += 0.002
                #print ('ai goes right')
                #print ('output val: ', output[0])
            if output[1] > 0.5:
                ai.left()
                ge[xx].fitness += 0.002
                #print ('ai goes left')
                #print ('output val: ', output[1])
            if output[2] > 0.5:
                #print ('ai_r1 ', aibul.ready)
                aibuls[xx].ready = False
                ge[xx].fitness += 0.003
                #print ('ai shots')
                #print ('output val: ', output[2])
                #print ('ai_r2 ', aibul.ready)

            if ge[xx].fitness <= -6:
                nets.pop(ais.index(ai))
                ge.pop(ais.index(ai))
                ais.pop(ais.index(ai))
            # draw ai
            #print ('fuking ai x after nn: ', ai.x)
            #aibul.ready = False
            #print ('fuking ai x after manual: ', ai.x)
            ai.draw(ai.x, ai.y)

            #ai shot
            #aibul.ready = False
            #print ('ai_r3 ', aibul.ready)
            aibuls[xx].draw(ai.x+16, ai.y-16)
        # collide
        for xx, ai in enumerate(ais):
            if collide(ai, b1bul, bot1):
                b1bul.y = bot1.y + 16
                b1score += 1
                ge[ais.index(ai)].fitness -= 1
                nets.pop(ais.index(ai))
                ge.pop(ais.index(ai))
                ais.pop(ais.index(ai))
                #print_score(p1score, aiscore)
            try:
                if collide(bot1, aibuls[xx], ais[xx]):
                    aibuls[xx].y = ai.y - 16
                    aiscore += 1
                    ge[ais.index(ai)].fitness += 1
                    #print_score(p1score, aiscore)
            except IndexError:
                print ("index error")
                pass
            except ValueError:
                print("value error")
                pass

        # generations
        score_label = stat_font.render("Gens: " + str(gen-1),1,(0,0,0))
        win.blit(score_label, (10, 500))
        # alive
        score_label = stat_font.render("Alive: " + str(len(ais)),1,(0,0,0))
        win.blit(score_label, (10, 550))
        
        score_label = stat_font.render("Bot: " + str(b1score),1,(0,0,0))
        win.blit(score_label, (780, 500))

        score_label = stat_font.render("AI: " + str(aiscore),1,(0,0,0))
        win.blit(score_label, (780, 550))
        
        # update display
        pygame.display.update()

if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)
