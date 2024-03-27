# densse NN works on global scale

# cnn - convolutional neural network. works on local scale.

# learns local patterns instead of whole image. Thus image flip doesn't affect to recgnition.
# image recognition

# three dimentions: image height, width, color channel

# each convolutional neural network is made up of one or many convolutional layers. These layers are different than the dense layers.
# Their goal is to find patterns from within images that can be used to classify the image or parts o it.

# convolution - extracts all features from photo

import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# load and split dataset
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
# normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

class_names = ['airplane', 'automobile', 'bird', 'cat', 'dog', 'deer',
                'dog', 'frog', 'horse', 'ship', 'truck']

# take a look at one image
img_index = 1
plt.imshow(train_images[img_index], cmap=plt.cm.binary)
plt.xlabel(class_names[train_labels[img_index][0]])
plt.show()

# CNN archotecture
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.conv2D(64, (3, 3), activation='relu'))

# look at model so far
model.summary()

# adding dense layers
model.add9layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10))
model.summary

# training
model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalcrossentropy(from_logits=True),
                metrics=['accuracy'])
history = model.fit(train_images, train_labels, epochs=10,
                    validation_data=(test_images, test_labels))

# evaluating the model
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(test_acc)


# working with small datasets
# data augmentation
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

# creates a data generator object that transforms images
datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

# pick an image to transform
test_img = train_images[14]
img = image.img_to_array(test_img)  # convert image to numpy array
img = img.reshape((1,) + img.shape) # reshape image

i = 0

# this loop runs forever until break, saving images to the urrent irrectory
for batch in datagen.flow(img, save_prefix='test', save_format='jpeg'):
    plt.figure(i)
    plot = plt.imshow(image.img_to_array(batch[0]))
    i += 1
    if i > 4:   # show 4 images
        break

plt.show()
