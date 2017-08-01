#!/usr/bin/env python
"""
Script to evaluate the NCDs for the violation versus
separation angle measurement

January 21, 2015
Author: Alessandro Cere, Centre for Quantum Technologies,
        National University of Singapore

"""
import glob

from bit_compression_analysis import *


angles = [x / 100. for x in range(0, 28, 2)]
angles[0] = 0
angles[8] = 0.15
angles[9] = 0.16
angles[10] = 0.18
angles[11] = 0.2
angles[12] = 0.22
angles[13] = 0.24

ncd_vec = []
compressor = 'lzma'

with open('result_' + compressor + '.dat', 'a') as f, \
        open('result_' + compressor + '_ncd.dat', 'a') as g:
    for angle in angles:

        str_a0b0_alice = str(angle) + '_a0b0_alice.dat.bin'
        str_a0b1_alice = str(angle) + '_a0b1_alice.dat.bin'
        str_a1b0_alice = str(angle) + '_a1b0_alice.dat.bin'
        str_a1b1_alice = str(angle) + '_a1b1_alice.dat.bin'

        str_a0b0_bob = str(angle) + '_a0b0_bob.dat.bin'
        str_a0b1_bob = str(angle) + '_a0b1_bob.dat.bin'
        str_a1b0_bob = str(angle) + '_a1b0_bob.dat.bin'
        str_a1b1_bob = str(angle) + '_a1b1_bob.dat.bin'

        str_a0b0_alice_bob = str(angle) + '_a0b0_alice_bob.dat.bin'
        str_a0b1_alice_bob = str(angle) + '_a0b1_alice_bob.dat.bin'
        str_a1b0_alice_bob = str(angle) + '_a1b0_alice_bob.dat.bin'
        str_a1b1_alice_bob = str(angle) + '_a1b1_alice_bob.dat.bin'

        a0b0_alice = glob.glob(str_a0b0_alice)[0]
        a0b1_alice = glob.glob(str_a0b1_alice)[0]
        a1b0_alice = glob.glob(str_a1b0_alice)[0]
        a1b1_alice = glob.glob(str_a1b1_alice)[0]

        a0b0_bob = glob.glob(str_a0b0_bob)[0]
        a0b1_bob = glob.glob(str_a0b1_bob)[0]
        a1b0_bob = glob.glob(str_a1b0_bob)[0]
        a1b1_bob = glob.glob(str_a1b1_bob)[0]

        a0b0_alice_bob = glob.glob(str_a0b0_alice_bob)[0]
        a0b1_alice_bob = glob.glob(str_a0b1_alice_bob)[0]
        a1b0_alice_bob = glob.glob(str_a1b0_alice_bob)[0]
        a1b1_alice_bob = glob.glob(str_a1b1_alice_bob)[0]

        c0, len_a0, na0, len_b0, nb0, len_ab0, nab0 = ncd_dist(
            a0b1_alice, a0b1_bob, a0b1_alice_bob, 1, compressor)
        c1, len_a1, na1, len_b1, nb1, len_ab1, nab1 = ncd_dist(
            a0b0_alice, a0b0_bob, a0b0_alice_bob, 1, compressor)
        c2, len_a2, na2, len_b2, nb2, len_ab2, nab2 = ncd_dist(
            a1b0_alice, a1b0_bob, a1b0_alice_bob, 1, compressor)
        c3, len_a3, na3, len_b3, nb3, len_ab3, nab3 = ncd_dist(
            a1b1_alice, a1b1_bob, a1b1_alice_bob, 1, compressor)

        ncd_vec.append(c0 - (c1 + c2 + c3))

        f.write(('{0} ' * 25 + '\n').format(angle, na0, nb0, nab0,
                                            na1, nb1, nab1,
                                            na2, nb2, nab2,
                                            na3, nb3, nab3,
                                            len_a0, len_b0, len_ab0,
                                            len_a1, len_b1, len_ab1,
                                            len_a2, len_b2, len_ab2,
                                            len_a3, len_b3, len_ab3))

        g.write('{0} {1}\n'.format(angle, c0 - (c1 + c2 + c3)))
