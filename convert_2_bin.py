#!/usr/bin/env python2

"""
Script to convert an ascii file to binary

January 21, 2015
Author: Alessandro Cere, Centre for Quantum Technologies,
        National University of Singapore

"""
import bitstring


def dat2bin(filename):
    """
    converts a ASCII file into a 8bit binary one.
    the output file is named as the input one plus .bin
    To avoid spurious correlations, instead of padding it drops the final bits
    not fytting into a full byte.
    """

    with open(filename) as fdat, open(filename + '.bin', 'wb+') as fbin:
        while True:
            a = fdat.read(8).strip()
            # reached EOF, stop converting
            if a == '':
                break

            # less than 8 bit, stop converting
            if len(a) < 8:
                break

            # converting to binary
            fbin.write(bitstring.BitArray('0b' + a).bytes)
