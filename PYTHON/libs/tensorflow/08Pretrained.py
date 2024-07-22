# use pretrained model

import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
keras = tf.keras

# dataset
import tensorflow_datasets as tfds
tfds.disable_progress_bar()

# split the data manualy into 80% train, 10% testng, 10% validation
(raw_train, raw_validation, raw_test), metadata = tfds.load(
        'cats_vs_dogs',
        split=['train[:80%]', 'train[80%:90%', 'train[90%]'],
        with_info=True,
        as_supervised=True,
        )

get_label_name = metadata.features['label'].int2str # create a function object that we can use to get labels

# diplay 2 images from the dataset
for image, label in raw_train.take(2):
    plt.figure()
    plt.imshow(image)
    plt.title(get_label_name(label))


# as images in different size, need to reshape them
img_size = 160          # all images will be resized 160x160

def format_example(image, label):
    '''
    returns an image that is reshaped to img_size
    '''
    image = tf.cast(image, tf.float32)
    image = (image/127.5) - 1
    image = tf.image.resize(image, (img_size, img_size))
    return image, label

# apply this function to all images using map
train = raw_train.map(format_example)
validation = raw_validation.map(format_example)
test = raw_test.map(format_example)

# have a look at images
for image, label in train.take(2):
    plt.figure()
    plt.imshow(image)
    plt.title(get_label_name(label))


# shuffle and batch the images
batch_size = 32
shuffle_buffer_size = 1000

train_batches = train.shuffle(shuffle_batch_size).batch(batch_size)
validation_batch = validation.batch(batch_size)
test_batches = test.batch(batch_size)

# orig vs new image shape
for img, label in raw_train.take(2):
    print("Original shape:", img.shape)
for img, label in train.take(2):
    print("New shape:", img.shape)

# picking a pretraained model
# mobile net v2 be used
img_shape = (img_size, img_size, 3)
# create the base model from the pretrained model MobileNet V2
base_model = tf.keras.applications.MobileNetV2(input_shape=img_shape,
                                                include_top=False,      # include classifier? False - No
                                                weighgts='imagenet')
base_model.summary()
# At this point this base_model will simply output a shape (32, 5, 5, 1280) tensor that is a feature extraction from
# original (1, 160, 160, 30 image.
# The 32 means that we have 32 layers of different filters/features.


# frize, not train
base_model.trainable = False

# adding needed (2 obgect) classifier
global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
predict_layer = keras.layers.Dense(1)
# combine these 2 layers together in a model
model = tf.keras.Sequential([
    base_model,
    global_average_layer,
    prediction_layer
    ])
model.summary()

# train the model (the rest 2 layers)
base_learning_rate = 0.0001
model.compile(optimizer=tf.keras.optimizer.RMSprop(lr=base_learning_rate),
                loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                metrics=['accuracy'])
# the train
history = model.fit(train_batches,
                    epoch=initial_epoch,
                    validation_data=validation_batches)
acc = history.history['accuracy']
print(acc)

# evaluate (check) the model
initial_epochs = 3
validation_steps = 20

loss0,accuracy0 = model.evaluate(validation_batches, steps = validation_steps)

# save specific for keras
model.save("dogs_vs_cats.h5")
new_model = tf.keras.models.load_model('dogs_vs_cats.h5')

