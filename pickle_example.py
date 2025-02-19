#!/bin/python3

import pickle

stuff = {"first_thing": 2525, "second_thing": 1991}
with open("stuff.pickle", "wb") as stuff_pickle:
    pickle.dump(stuff, stuff_pickle)