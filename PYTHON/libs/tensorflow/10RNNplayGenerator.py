# prdicts most likely next character
# trained on Romeo&Juliet

from keras.preprocessing import sequence
import keras
import tensorflow as tf
import os
import numpy as np


# dataset
# downloading
path_to_file = tf.keras.utils.get_file('shakespare.txt', 'https://storage.googleapis.com/download.tensorflow.org/data/shakespare.txt')
'''
# load own files
from google.collab import files
path_to_file = list(files.upload().keys())[0]
'''

# read content of the file
# read then decode for py2 py2 compat.
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
# length of text is the number of characters in it
print('Length of text: {} characters'.format(len(text)))
# take a look at the first 250 chars
print(text[:250])

# encoding
# since this text isn't encoded yet we'll need to do that ourself.
# encode each unique character as a different intger.
vocab = sorted(set(text))
# creating a mapping from unique characters to indices
char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)
def text_to_int(text):
    return np.array([char2idx[c] for c in text])
text_as_int = text_to_int(text)

# look at how part of our text is encoded
print("Text:", text[:13])
print("Enccoded:", text_to_int(text[:13]))

# decode
def int_to_text(ints):
    try:
        ints = ints.numpy()
    except:
        pass
    return ''.join(idx2char[ints])
print(int_to_text(text_as_int[:13]))

# creating training examples
seq_length = 100        # length of sequence for a training example
examples_per_epoch = len(text)//(seq_length+1)
# creating training examples / targets. in other words - convert text into haraters
char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)
# now can use the batch method to turn this stream of characters into batches of desired length
sequences = char_dataset.batch(seq_length+1, drop_remainder=True)
# now need to use these sequences of length 101 and split them into input and output
def split_input_target(chank):      # for the example: hello
    input_text = chunk[:-1]         # hell
    target_text = chunk[1:]         # ello
    return input_text, target_text  # hell, ello
dataset = sequence.map(split_input_target)  # we use map to apply the above function to every entry
# print example
for x, y in dataset.take(2):
    print("\n\nExample\n")
    print("Input")
    print(int_to_text(x))
    print("\nOutput")
    print(int_to_text(y))

# finaly make training batches
batch_size = 64
vocab_size = len(vocab) # vocab is number of unique characters
embedding_dim = 256     # emb dimention
rnn_units = 1024
# buffer sie to shuffle dataset
# (TF data is designed to work with pssibly infinite sequences
# so it doesn't attempt to shuffle the entire sequene in memory.
# Instead, it maintains a buffer in which it shuffle elements).
buffer_size = 10000

data = dataset.shuffle(buffer_size).batch(batch_size, drop_remainder=True)

# building the model
def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size, embedding_dim,
            batch_input_shape=[batch_size, None]),              # we dont know how long it be, so None is here
        tf.keras.layers.LSTM(rnn_units,
            return_sequences=True,
            stateful=True,
            recurent_initializer='glorot_uniform'),
        tf.keras.layers.Dence(vocab_size)
        ])
    return model

model = build_model(vocab_size, embedding_dim, rnn_units, batch_size)
model.summary()


# lets have a look at a sample input and the output from untrained model
for input_example_batch, target_example_batch in data.take(1):
    example_batch_predictions = model(input_example_batch)  # ask our model for a prediction on our first batch of training data
    print(example_batch_predictions.shape, "# (batch_size, seqquential_length, vocab_size)")    # print out the output shape
    # can see that the predictions is an array of 64 arrays, one for each entry in the batch
    print(len(example_batch_predictions))
    print(example_batch_predictions)
    # lets examine one predictiond
    pred = example_batch_predictions[0]
    print(len(pred))
    print(pred)
    # notice this is a 2d array of length 100, where each interior array is the prediction for the next character at each time step

# and finaly weell look at a prediction at a wery first timestep
time_pred = pred[0]
print(len(time_pred))
print(time_pred)
# an ofource its 65 values representing the probability of each character ocuring next

# if want to determine the predicted character we need to sample the output distribution (pick a value based on probabillities)
sample_indices = tf.random.categorical(pred, num_samples=1)
# now we can reshape that array and convert all the integers to numbers to see the actual characters
sampled_indices = np.reshape(sampled_indices, (1, -1))[0]
predicted_chars = int_to_text(sampled_indices)
predicted_chars # and this is what the model predicted for training equence 1


# creating a loss function
def loss(labels, logits):
    return tf.keras.losses.sparce_categorical_crossentropy(labels, logits, from_logits=True)

# compiling the model
model.compile(optimizer='adam', loss=loss)

# creating chepoints
# diretory where the checkpoints wil be saved
checkpoint_dir = './training_checkpoints'
# name of the checkpoint files
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

checkpoint_callback = tf.keras.callbacks.ModelChekpoint(
        filepath=checkpoint_prefix,
        save_weights_only=True)

# training
history = model.fit(data, eposhs=40, callbacks=[checkpoint_callback])

# loading the model
model = build_model(vocab_size, embedding_dim, rnn_units, bath_size=1)
# once the model is finished training we can find the latest checkpoint that stores the models weighgts using the following line
model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))
model.build(tf.TensorShape([1, None]))
# can load any checkpoint we want by specifying tha exact file to load.
checkpoint_num = 10
model.load_weights(tf.train.load_chekpoint("./training_checkpoints/ckpt_" + str(checkpoint_num)))
model.build(tf.TensorShape([1, None]))


# generating text
# use lovely function provided by tensorflow
def generate_text(model, start_string):
    # evaluation step (generating text using the learned model)
    # number f character to generate
    num_generate = 800

    # converting our start string to numbers (vectorizing)
    input_eval = [char2idx[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)
    # empty string to store our results
    txt_generated = []

    # low temperatures result in more predictable text.
    # Higher temperatures results in more surprising text.
    # Experiment to find the best setting
    temperature = 1.0

    # Here batch size == 1
    model.reset_states()
    for i in range(num_generate):
        predictions = model(input_eval)
        # remove the batch dimention
        predictions = tf.squeeze(predictions, 0)

        # using a categorical disttribution to predict the character returned by the model
        predictions = predictions / temperature
        predicted_id = t.random.categorical(predictions, num_samples=1)[-1,0].numpy()

        # we pass the predicted haracters as a next input to the model
        # along with the previous hidden state
        input_eval = tf.expand_dims([predicted_id], 0)
        text_generated.append(idx2char[predicted_id])
    return (start_string + ''.join(text_generated))

inp = input("Type a starting string: ")
print(generate_text(model, inp))


