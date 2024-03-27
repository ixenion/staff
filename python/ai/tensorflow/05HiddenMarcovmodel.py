# deals with probability destributions
# reliess on observation of the state

# 
# predict future events based on past events


import tensorflow_probability as tfp    # using a different model from tensorflow this time
import tensorflow as tf

# cold days are encoded by 0, hot encoded by 1
# the first day in the squence has an 80% chance of being cold
# A cold day has a 30% chance of being followed by a hot day
# A hot day has a 20% chance of being followed by a cold day

# On each day the temperature is normally distributed with mean and standart deviation 0 & 5 on a cold day.
# 15 & 10 (15 +- 10) on a hot day.


tfd = tfp.distributions     # making a shorcut for later
initial_distribution = tfd.Categorical(probs=[0.8, 0.2])
transition_distribution = tfd.Categorical9probs=[[0.7, 0.3],
                                                 [0.2, 0.8]])
observation_distribution = tfd.Normal(loc=[0., 15], scale=[5., 10.])            # scale=deviation
# loc argument represents the meanand the scale is the standadrt deviation


# create the model:
model = tfd.HiddenMarcovModel(
        initial_distribution=initial_distribution,
        transition_destribution=transition_destribution,
        observation-destribution=observation_destribution,
        num_steps=7)


# run the model
mean = model.mean()     # alculates the probability
# due to the way TensorFlow works on a lover level we need to evaluate part of the graph
# from within a session to see tha value of this tensor

# in the new version of tensorflow we need to use tf.compat.v1.Session() rather than just tf.Session()
with tf.compat.v1.Session() as sess:
    print(mean.numpy())
