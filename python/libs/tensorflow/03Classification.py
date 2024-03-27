
# separates flowers into 3 different classes of species:
# Setosa, Versicolor, Virginica

# information about each flower:
# sepal length
# sepal width
# petal length
# petal width


from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import pandas as pd


# define column names
csv_column_names = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']
species = ['Setosa', 'Versicolor', 'Virginica']

# LOAD DATASETS
train_path = tf.keras.utils.get_file(
        "iris_training.csv", "https://storage.googleapis.com/download.tensorflow.org/data/iris_training.csv"]
test_path = tf.keras.utils.get_file(
        "iris_test.csv", "https://storage.googleapis.com/download.tensorflow.org/data/iris_test.csv"]

# use keras (a module inside of tensorflow) to grab datasets and read them into a pandas dataframe
train = pd.read_csv(train_path, names=csv_column_names, header=0)
test = pd.read_csv(test_path, names=csv_column_names, header=0)

# to look at this data
train.head()

# pop the species column off
# and use it as a label
train_y = train.pop('Species')
test_y = test.pop('Species')
# check train shape
train.shape


# INPUT FUNCTION
def input_fn(features, labels, training=True, batch_size=256):
    # Convert the inputs to a Dataset
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    # Shuffle & repeat if you are in training mode
    if training:
        dataset = dataset.shuffle(1000).repeat()

    return dataset.batch(batch_size)

# feature columns desribe how to use the input
my_feature_columns = []
for key in train.keys():        # key = feature
    my_feature_columns.append(tf.feature_column.numeric_column(key=key))
#print(my_feature_columns)


# BUILDING A MODEL
# examples: LinearClassifier, DNNClassifier (Deep Neural Network)
# DNN may be better becouse there may not be an linear corespondence in the data
# DNN with 2 hidden layers with 30 & 10 hidden nodes each
classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        # two hidden layers of 30 & 10 nodes respectively
        hidden_units=[30,10],
        # the model must choose between 3 classes
        n_classes=3)


'''
lambda function:
x = lambda: print("hi")
x()
'''

# TRAIN CLASSIFIER
classifier.train(
        input_fn=lambda: input_fn(train, train_y, training=True),
        steps=5000)



# TEST
eval_result = classifier.evaluate(
        input_fn=lambda: input_fn(test, test_y, training=False))
print('\nTest set accuracy: {accuraccy:0.3f}\n'.format(**eval_result))


# PREDICTIONS
def input_fn(features, batch_size=256):
    # Convert the inputs to a Dataset without labels
    return tf.data.Dataset.from_tensor_slices(dict(features)).batch(batch_size)

features = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']
predict = {}

print("please type numeric values as prompted.")
for feature in features:
    valid = True
    while valid:
        val = input(feature + ": ")
        if not val.isdigit(): valid=False

    predict[feature] = [float(val)]

predictions = classifier.predict(input_fn=lambda: input_fn(predict))
for pred_dict in predictions:
    class_id = pred_dict['class_ids'][0]
    probability = pred_dict['probabilities'][class_id]

    print('Predictions  is "{}" ({:.1f}%)'.format(
        species[class_id], 100 * probability))


