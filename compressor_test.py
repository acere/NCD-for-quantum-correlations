#!/usr/bin/env python2

"""
Script to run the compressibility versus string length test
and compressibility versus correlation test
for various compressors

January 21, 2015
Author: Alessandro Cere, Centre for Quantum Technologies,
        National University of Singapore

"""
import glob
from bit_compression_analysis import *

"""
defining list of filenames of file to compress
for compressibility versus string length test
"""
filename_list = [pow(10, x) for x in range(3, 8, 1)]

# # for compressibility versus correlation test
# filename_list = [x/100. for x in range(0, 51, 1)]
# filename_list[0] = 0

# defining compressor to use
compressor = 'lzma'

# writing result to output file
with open('result_' + compressor + '.dat', 'a') as f:
    for filename in filename_list:
        str_file = str(filename) + '_output.bin'
        str_array = glob.glob(str_file)[0]
        len_a0, na0 = comp_ratio(str_array, 1, compressor)
        f.write('{0} {1} \n'.format(filename, na0, len_a0,))
