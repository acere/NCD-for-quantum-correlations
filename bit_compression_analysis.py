#!/usr/bin/env python2
"""
Script to compress binary files, using various compressors,
containing string of various length and
return the compressed and original string length


January 21, 2015
Author: Alessandro Cere, Centre for Quantum Technologies,
        National University of Singapore

"""

import zlib
import bz2
import os
import pylzma
import lzw


"""defining routines for various compressors"""


def lzw_len(filename):
    """
    Calculates the length of the string resulting from compressing
    the input file using lzw compressor

    :param filename: input file
    :return: length of the compressed buffer
    """
    buffer_v = lzw.readbytes(filename)
    compressed_buffer = lzw.compress(buffer_v)
    return len([x for x in compressed_buffer])


def pylzma_len(filename):
    """
    Calculates the length of the string resulting from compressing
    the input file using lzma compressor

    :param filename: input file
    :return: length of the compressed buffer
    """
    return len(pylzma.compress(open(filename, 'U').read()))


def gzip_len(filename):
    """
    Calculates the length of the string resulting from compressing
    the input file using gzip compressor

    :param filename: input file
    :return: length of the compressed buffer
    """
    return len(zlib.compress(open(filename, 'U').read()))


def bz2_len(filename):
    """
    Calculates the length of the string resulting from compressing
    the input file using bz2 compressor

    :param filename: input file
    :return: length of the compressed buffer
    """
    return len(bz2.compress(open(filename, 'U').read()))


def comp_ratio(files_a, print_out, compressor=bz2):
    """
    function to calculate the compressed and original length of files_a
    :return: the NCD distance as a float()
    """
    if compressor == 'lzma':
        comp_f = pylzma_len
    elif compressor == 'lzw':
        comp_f = lzw_len
    elif compressor == 'gzip':
        comp_f = gzip_len
    else:
        comp_f = bz2_len

    len_a = os.path.getsize(files_a)
    if len_a == 0:
        len_a = 1

    na = comp_f(files_a)

    if print_out:
        print(comp_f)
        print('String A reduced from {0} to {1}, {2:.1f}%]'.format(
            len_a, na, 100.0 * na / len_a))

    return len_a, na


def ncd_dist(files_a, files_b, files_ab, print_out=0, compressor=bz2):
    """
    function to evaluate the NCD of two files and returns
    their compressed and original length

    :param files_a: first file
    :param files_b: second file
    :param files_ab: file obtained by joining files a and b
    :param print_out: flag to turn on verbose output
    :param compressor: choice of compression algorithm. Default is bz2
                       other options are lzma, lzw, and gzip
    :return: NCD, length of a, C(a), b, C(b), a+b, C(a+b)
    :return type: float, int, int, int, int, int, int
    """
    if compressor == 'lzma':
        comp_f = pylzma_len
    elif compressor == 'lzw':
        comp_f = lzw_len
    elif compressor == 'gzip':
        comp_f = gzip_len
    else:
        comp_f = bz2_len

    len_a = os.path.getsize(files_a)
    if len_a == 0:
        len_a = 1

    len_b = os.path.getsize(files_b)
    if len_b == 0:
        len_b = 1

    len_ab = os.path.getsize(files_ab)
    if len_ab == 0:
        len_ab = 1

    na = comp_f(files_a)
    nb = comp_f(files_b)
    nab = comp_f(files_ab)

    if print_out:
        print(comp_f)
        print('String A reduced from {0} to {1}, {2:.1f}%]'.format(
            len_a, na, 100.0 * na / len_a))
        print('String B reduced from {0} to {1}, {2:.1f}%]'.format(
            len_b, nb, 100.0 * nb / len_b))
        print('String AB reduced from {0} to {1}, {2:.1f}%]'.format(
            len_ab, nab, 100.0 * nab / len_ab))

    return (nab - min(na, nb)) / (1.0 * max(na, nb)),\
        len_a, na, len_b, nb, len_ab, nab
