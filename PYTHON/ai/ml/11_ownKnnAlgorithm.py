import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

dataset = {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
new_features = [5,7]
print(len(dataset))
def k_nearest_neighbors(data, predict, k=5):
    if len(data) >= k:
        warnings.warn('K is set to a value less then total voting groups!')
    distances = []
    for group in data:
        for features in data[group]:

            #long method, and uses only two dimentional data features
            #euclidean_distance = sqrt( (features[0]-predict[0])**2 +(features[1]-predict[1])**2 )
            
            #better, could assume more dimentional features, but long
            #euclidean_distance = np.sqrt(np.sum((np.array(features)-np.array(predict))**2))
            
            #best
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance, group])

    votes = [i[1] for i in sorted(distances)[:k]]
    print(Counter(votes).most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]

    return vote_result

result = k_nearest_neighbors(dataset, new_features, k=5)
print(result)

[[plt.scatter(ii[0],ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
plt.scatter(new_features[0], new_features[1], color=result)
plt.show()
