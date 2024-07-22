import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
import pandas as pd
import random
style.use('fivethirtyeight')

def k_nearest_neighbors(data, predict, k=5):
    if len(data) >= k:
        warnings.warn('K is set to a value less then total voting groups!')
    distances = []
    for group in data:
        for features in data[group]:            
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance, group])

    votes = [i[1] for i in sorted(distances)[:k]]
    print(Counter(votes).most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]

    return vote_result

df = pd.read_csv('csv/breastCancer.txt')#25
df.replace('?', -99999, inplace=True)#26
df.drop(['id'], 1, inplace=True)#27
full_data = df.astype(float).values.tolist()
random.shuffle(full_data)
#lines 25,26,27 could be writen in one line:
#df = pd.read_csv('csv/breastCancer.txt', na_values='?', header=0).fillna(-99999).drop('id', axis=1)

test_size = 0.2
train_set = {2:[], 4:[]}
test_set = {2:[], 4:[]}
train_data = full_data[:-int(test_size*len(full_data))]
test_data = full_data[-int(test_size*len(full_data)):]

for i in train_data:
    train_set[i[-1]].append(i[:-1])

for i in test_data:
    test_set[i[-1]].append(i[:-1])

correct = 0
total = 0

for group in test_set:
    for data in test_set[group]:
        vote = k_nearest_neighbors(train_set, data, k=5)
        if group == vote:
            correct += 1
        total += 1

print('Accuracy: ', correct/total)

