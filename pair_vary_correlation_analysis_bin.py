#!/usr/bin/env python
"""
Script to compress files containing consecutive pair
with various probability of correlation

January 21, 2015
Author: Alessandro Cere, Centre for Quantum Technologies,
        National University of Singapore

"""

import glob
from bit_compression_analysis import *

probs = [x / 100. for x in range(0, 51, 1)]
probs[0] = 0

compressor = 'lzma'

with open('result_' + compressor + '.dat', 'a') as f:
    for prob in probs:
        str_file = str(prob) + '_output.dat.bin'
        str_array = glob.glob(str_file)[0]
        len_a0, na0 = comp_ratio(str_array, 1, compressor)
        f.write('{0} {1} {2}\n'.format(prob, na0, len_a0,))
