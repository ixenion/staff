# Natural Language Processing

# using recurrent neural network
# spell check, autoccomlete, voise assistance, translation between languages, chat bots

# current topicks:
# sentiment analysis (positive or negative sentance)
# Character Generation (generate next symbol in a sequence of text)

# based of movie review dataset (contains 25k reviews)

from keras.dataset import imdb
from keras.preprocessing import sequence
import tensorflow as tf
import os
import numpy as np

vocab_size = 88584

maxlen = 250
batch_size = 64

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words = voab_size)
# look at one review
print(train_data[0])

# preprocessing     sentence length is differ, that's a problem
# if the review is greater than 250 words then trim off extra words
# if the review is less than 250 words add the neccessary amount of 0's to make it equal to 250 
train_data = sequence.pad_sequence(train_data, maxlen)
test_data = sequence.pad_sequence(test_data, maxlen)

# creating the model
model = tf.keras.Sequential([
                            tf.keras.layers.Embedding(vocab_size, 32),
                            tf.keras.layers.LSTM(32),
                            tf.keras.layers.Dense(1, activation='sigmoid')
                            ])
print(model.summary())

# training
model.compile(loss="binary_crossentropy",optimizer="rmsprop",metrics=['acc'])
history = model.fit(train_data, train_labels, epochs=10, validation_split=0.2)

# evaluate the model on training data to see how well it performs
results = model.evaluate(test_data, test_labels)
print(results)


# making predictions
word_index = imdb.get_word_index()
def encode_text(text):
    tokens = keras.preprocessing.text.text_to_word_sequence(text)
    tokens = [word_index[word] if word in word_index else 0 for word in tokens]
    return sequence.pad_sequences([tokens], maxlen)[0]

text = "that movie was amazing, so amazing"
encoded = encode_text(text)
print(encoded)

# while were at it lets make a decode function
reverse_word_index = {value: key for (key, value) in word_index.items()}
def decode_integers(integers):
    pad = 0
    text = ""
    for num in integers:
        if num != pad:
            text += reverse_word_index[num] + " "

    return text[:-1]
print(decode_integers(encoded))


# time to make a prediction
def predict(text)::
    encoded_text = encode_text(text)
    pred = np.zeros((1,250))
    pred[0] = encoded_text
    result = model.predict(pred)
    print(result[0])

positive_review = "That was so awesome! I really loved it an would watch it again because it was amaizingly great"
predict(positive_review)

neg_review = "that movie sucked. I hated it and wouldn't watch it again. Was one of the wowrst thing I've ever watched"
predict(neg_review)

