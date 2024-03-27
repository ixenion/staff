import os
import pickle

scores = {}
#target = 'best.pickle'
target = 'winner.pickle'

if os.path.getsize(target) > 0:
    with open(target, "rb") as f:
        unpickler = pickle.Unpickler(f)
        scores = unpickler.load()
        print ('unpikled ', os.path.getsize(target))
        print (scores)
