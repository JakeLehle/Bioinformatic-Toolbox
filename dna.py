#!/usr/bin/env python3
"""
Author : DNA <admin-jdl@localhost>
Date   : 2021-10-17
Purpose: Tetranucleotide_frequency
"""
import os
import argparse
from typing import NamedTuple

class Args(NamedTuple):
    """ Command-line arguments """
    dna: str
    

# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Tetranucleotide_frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna',
                        metavar='DNA',
                        help='Input DNA sequence')

    args = parser.parse_args()
    
    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()

    return Args(args.dna)

# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    count_a, count_c, count_g, count_t = 0, 0, 0, 0
    
    for base in args.dna:
        if base == 'A':
            count_a += 1
        elif base == 'C':
            count_c += 1
        elif base == 'G':
            count_g += 1
        elif base == 'T':
            count_t += 1

    print(f'A:C:G:T = "{count_a}", "{count_c}", "{count_g}", "{count_t}"')

# --------------------------------------------------
if __name__ == '__main__':
    main()
