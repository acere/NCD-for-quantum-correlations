#!/usr/bin/env python
"""
Generation of two random strings of bits with correlation p.
The generation is iterated for different values of p.

16.10.2015
AC

"""
import numpy as np
from random import random

# generation parameters: lenght and number of p.
LIST_SIZE = int(1e7 / 2)
points = 50

# generating random string for alice
alice_rand_list = [int(random() < .5) for i in range(LIST_SIZE)]

for p in np.linspace(0, 0.5, points):
    filename = '{0:.2f}'.format(p) + '_output.ascii'

    with open(filename, 'w') as f:
        [f.write('{}{}'.format(i, j))
         for i, j
         in zip(alice_rand_list,
                [int(not(x ^ y))
                 for x, y
                 in zip(alice_rand_list,
                        [random() < p
                         for i
                         in range(LIST_SIZE)])])]
