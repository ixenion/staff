import gym
import numpy as np
from IPython.display import clear_output
from time import sleep

env = gym.make("Taxi-v35").env
#env.render()

#env.reset() # reset environment to a new, random state
#env.render() # render

# additional information
#print("Action Space {}".format(env.action_space))
#print("State Space {}".format(env.observation_space))

# action space
# 0-south 1-north 2-east 3-west 4-pickup 5-dropoff

# encode state manualy
state = env.encode(3, 1, 2, 0) # (taxi row, taxi column, passenger index, destination index)
print("State: ", state)
env.s = state
env.render()

input('Start eval:')

# print current environment Reward table (states x actions)
#print("Reward table")
#print(env.P[328])
# the dictionary has the structure
# {action: [(probability, next state, reward, done)]}

###########################
# save and load the model #
###########################

# save to csv
#from numpy import savetxt
#savetxt('q_table.csv', q_table, delimiter=',')

# load from csv
#from numpy import loadcsv
#q_table = loadtxt('q_table', delimiter=',')

# save to .npy (binary)
#from numpy import save
#save('q_table.npy', q_table)

# load from .npy (binary)
#from numpy import load
#q_table = load('q_table.npy')

# save to .npz (compressed)
#from numpy import savez_compressed
#savez_compressed('q_table.npy', q_table)

# load from .npy (compressed)
from numpy import load
# load dict of arrays (savez may store multiple arrays at one .npz)
dict_q_table = load('q_table_80k.npz')
q_table = dict_q_table['arr_0']

###########################

# evaluate (test) agent's performance after q-learning
total_epochs, total_penalties = 0,0
episodes = 100
frames = [] # for animation
not_passed = 0
for _ in range(episodes):
    state = env.reset()
    epochs, penalties, reward = 0,0,0

    done = False

    while not done:
        action = np.argmax(q_table[state])
        state, reward, done, info = env.step(action)
        if reward == -10:
            penalties += 1
        
        # put each rendered frame into dict for animation
        frames.append({
            'frame': env.render(mode='ansi'),
            'state': state,
            'action': action,
            'reward': reward
            }
        )
        
        #print('epochs', epochs)
        #print('done', done)
        #sleep(1)
        epochs += 1
        if epochs >= 20:
            #print('[!] episode ',_)
            #print('    Eval taking over 20 epochs, leaving')
            not_passed += 1
            break

    total_penalties += penalties
    total_epochs += epochs

print(f"Result after {episodes} episodes:")
print(f"Average timesteps per episode: {total_epochs / episodes}")
print(f"Average penalties per episone: {total_penalties / episodes}")

sleep(2)
# to visualize
def print_frames(frames):
    for i, frame in enumerate(frames):
        clear_output(wait=True)
        #env.render()
        print(frame['frame'])
        print(f"Timestep: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(1)

print('not_passed: ', not_passed)
#print(q_table[328])
print_frames(frames) # sleep timer at this function

