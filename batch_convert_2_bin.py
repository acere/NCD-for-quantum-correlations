#!/usr/bin/env python
"""
Script to run through all files with .dat and convert them to binary

January 21, 2015
Author: Alessandro Cere, Centre for Quantum Technologies,
        National University of Singapore

"""
import glob
from convert_2_bin import dat2bin

for filen in glob.glob("*.dat"):
    print(filen)
    dat2bin(filen)  # calling conversion routine
