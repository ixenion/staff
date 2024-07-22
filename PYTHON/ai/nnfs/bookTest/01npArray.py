import numpy as np

a = [1,2,3]

print(np.array(a))
print(np.array([a]))
print(type(np.array(a)))
print(type(np.array([a])))

print(np.expand_dims(np.array(a), axis=0))
print(np.expand_dims(np.array(a), axis=1))
print(np.expand_dims(np.array(a), axis=2))
