#!/usr/bin/env python3
""" Tetranucleutide frequency """

import argparse
#------------------------------------------------------------------------------
def get_args():
    """Get command-line arguments"""
    
    parser = argparse.ArgumentParser(
        description='Tetranucleutide frequency', 
        formatter_class=argparse.ArgumentDefaultHelpFormatter)
    
    parser.add_argument('dna', metvar ='DNA', help='Input DNA sequence')
    
    return parser.parse_args()

#------------------------------------------------------------------------------
def main():
    """Program start"""
    
    args = get_args()
    print(args.dna)
    
#------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
