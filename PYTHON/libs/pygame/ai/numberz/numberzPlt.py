import matplotlib.pyplot as plt
import numpy as np

test_data_file = open("/home/porter/project/ml/csv/mnist_test_10.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

all_values = test_data_list[1].split(',')
print(all_values[1])

image_array = np.asfarray(all_values[1:]).reshape((28,28))
plt.imshow(image_array, cmap='Greys', interpolation='None')
plt.show()
