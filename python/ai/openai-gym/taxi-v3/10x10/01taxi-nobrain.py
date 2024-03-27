import gym

env = gym.make("Taxi-v310").env
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
input('solve evn without learning')
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
input('visualize:')
# visualize
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

