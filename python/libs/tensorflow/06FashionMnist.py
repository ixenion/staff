
import tensorflow as tf
from tensorflow import keras

# helper libs
import numpy
import matplotlib.pyplot as plt


# load dataset
fashion_mnist = keras.dataset.fashion_mnist     # network needed
# split into training and tsting
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# look at the data
train_images.shape      # 60k imgs, 28x28, tot 784 each
# pixel values are between 0 and 255. 0 - blak, 255 - white. gray scale img, no color
# look at one pixel
train_images[0,23,23]

# have a look at the first 10 training labels
train_labels[:10]

# labels are integers from 0-9. each integer represents a specific article of closing. Create an array of label nams to indicate
# which is which.
class_names = ['T-shirt/top', 'Troser', 'Pullover', 'Dress', 'Coat',
                'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# plot image
plt.figure()
plt.imshow(train_images[1])
plt.colorbar()
plt.grid(False)
plt.show()


# Data preprocessing
train_images = train_images / 255.0
test_images = test_images / 255.0

# building the model
model = keras.sequential([
    keras.layers.Flatten(input_shape=(28, 28)),     # input layer (1)
    keras.layer.Dense(128, activation='relu'),      # hidden layer (2)
    keras.layer.Dense(10, activation='softmax')
    ])


# Compile the model
model.compile(optimizer='adam',
        loss='sparse_ategorical_crossentropy',
        metrics=['accuracy'])


# training the model
model.fit(train_images, train_labels, epochs=10)

# evaluating the model
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=1)
print('Test accuracy:', test_acc)

# prediction
predictions = model.predict(test_images)
#test_images.shape
print(predictions[0])
print(np.argmax(predictions[0]))     # returns the max index

# assign the class
print(class_names[np.argmax(predictions[0])])



# easy check
color = 'white'
plt.rcparams['test.color'] = color
plt.rcParams['axes.labelcolor'] = color

def predict(model, image, correct_label):
    class_names = ['T-shirt/top', 'Troser', 'Pullover', 'Dress', 'Coat',
                'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    prediction = model.predict(np.array([image]))
    predicted_class = class_names(np.argmax(prediction)]

    show_image = (image, class_names[correct_label], predict_class)

def show_image(img, label, guess):
    plt.figure()
    plt.imshow(img, cmap=plt.cm.binary)
    plt.title("excpected: " + label)
    plt.xlabel("Guess: " + guess)
    plt.colorbar()
    plt.grid(False)
    plt.show()

def get_number():
    while True:
        num = input("Pick a number: ")
        if num.isdigit():
            num = int(num)
            if 0 <= num <= 1000:
                return int(num)
            else:
                print("Try again...")

num = get_number()
image = test_images[num]
label = test_labels[num]
predict(model, image, label)

