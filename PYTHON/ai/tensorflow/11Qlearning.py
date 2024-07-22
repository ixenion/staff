# Q - Learning
# or Reinforsment learning

# used for games
# rather than feeding our machine learning model milions of examples we let our model come up with it's own examples by exploring an environment

'''
import gym  # all you have to do import and use open ai gym

env = gym.make('FrozenLake-v0') # we are going to use the FrozenLake Environment
# there are a few more cmmands that can be used to interact and get information about the Environment
print(env.observation_space.n)  # get number of states
print(env.action_space.n)   # get number of actions
env.reset() # reset environment to default state
action = env.action_space.sample()  # get a random action
print(action)

# did we loose the game (gameover)? if so - done = True
new_state, reward, done, info = env.step(action)  # take ation, notice it returns information about the action

env.render()    # render the GUI for the environment. Disable to save resources
'''

# frozen lake environment
import gym
import numpy as np
import time

states = env.observation_space.n
action = env.action_space.n
Q = np.zeros((state, action))   # create a matrix with all 0 values

# constants
episodes = 2000 # how many times to run the environment from the beginning
max_steps = 100 # max number of steps allowed for each run of environment
render = False

learning_rate = 0.81
gamma = 0.96

# picking an action
epsilon = 0.9   # start with a 90% chance of piking a random action

'''
# code to pick action
if np.random.uniform(0, 1) < epsilon:   # we will check if a random selected value is less than epsilon.
    action = env.action_space.sample()  # take random action
else:
    action = np.argmax(Q[state, :]) # use Q table to pick best action based on current values
'''


# updating Q values

rewards = []
for episode in range(episodes):
    state = env.reset()
    for _ in range(max_steps):
        if render:
            env.render()
        if np.random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()  # take random action
        else:
            action = np.argmax(Q[state, :]) # use Q table to pick best action based on current values

        new_state, reward, done, _ = env.step(action)  # take ation, notice it returns information about the action
        Q[state, action] + learning_rate * (reward + gamma * np.max(Q[new_state, :]) - Q[state, action])
        state = next_state

        if done:
            rewards.append(reward)
            epsilon -= 0.001
            break   # reached goal
print(Q)
print(f"Average reward: {sum(rewards)/len(rewards)}:")
# and now we can see our Q walues

# an plot the training progress and see how the agent improved
import matplotlib.pyplot as plt

def get_average(values):
    return sum(values)/len(values)

avg_rewards = []
for i in range(0, len(rewards), 100):
    avg_reward.append(get_average(rewards[i:i+100]))

plt.plot(avg_rewards)
plt.ylabel('average reward')
plt.xlabel('episodes (100\'s)')
plt.show()



