import gym

env = gym.make("Taxi-v35").env
env.render()

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

# print current environment Reward table (states x actions)
print("Reward table")
print(env.P[328])
# the dictionary has the structure
# {action: [(probability, next state, reward, done)]}

# solving the environment without learning
env.s = 328
epochs = 0
penalties, reward = 0, 0
frames = [] # for animation
done = False

'''
# random (not learned) model
while not done:
    action = env.action_space.sample() # random action
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

    epochs += 1

print("Timesteps taken: {}".format(epochs))
print("Penalties incurred: {}".format(penalties))
# out something like 1117, 363

# visualize random model
from IPython.display import clear_output
from time import sleep

def print_frames(frames):
    for i, frame in enumerate(frames):
        clear_output(wait=True)
        #env.render()
        print(frame['frame'])
        print(f"Timestep: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(.5)

print_frames(frames)
'''

# train the model
import numpy as np
q_table = np.zeros([env.observation_space.n, env.action_space.n])
#%%time
import random
from IPython.display import clear_output
from time import sleep

# hyperparameters
alpha = 0.1 # learning rate
gamma = 0.6 #
epsilon = 0.1 # 

# for plotting metrics
all_epochs = []
all_penalties = []

for i in range(80001):
    state = env.reset()

    epochs, penalties, reward = 0,0,0
    done = False

    while not done:
        if random.uniform(0,1) < epsilon:
            action = env.action_space.sample() # explore action space
        else:
            action = np.argmax(q_table[state]) # exploit learned values

        next_state, reward, done, info = env.step(action)

        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])

        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[state, action] = new_value

        if reward == -10:
            penalties += 1

        state = next_state
        epochs += 1

    if i % 100 == 0:
        clear_output(wait=True)
        print(f"Episode: {i}")

print("Training finished.\n")

# now q_table has been established over 100 000 episodes
# to see what the q-values are at illustration's state
#print(q_table[328])

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
from numpy import savez_compressed
savez_compressed('q_table_80k.npz', q_table)

# load from .npy (compressed)
#from numpy import load
# load dict of arrays (savez may store multiple arrays at one .npz)
#dict_q_table = load('q_table.npy')
#q_table = dict_q_table['arr_0']

###########################
'''
# evaluate (test) agent's performance after q-learning
total_epochs, total_penalties = 0,0
episodes = 1

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
            print('Something went wrong while eval')
            break

    total_penalties += penalties
    total_epochs += epochs

print(f"Result after {episodes} episodes:")
print(f"Average timesteps per episode: {total_epochs / episodes}")
print(f"Average penalties per episone: {total_penalties / episodes}")

#sleep(5)
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
        sleep(1.5)

#print(q_table[328])
#print_frames(frames) # sleep timer at this function
'''
