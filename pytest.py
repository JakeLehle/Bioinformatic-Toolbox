#!/usr/bin/env python3
"""
Author : admin-jdl <admin-jdl@localhost>
Date   : 2021-10-23
Purpose: Rock the Casbah
"""
import os
import platform
from subprocess import getstatusoutput
PRG = './dna.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
TEST1 = ('./tests/inputs/input1.txt')
TEST2 = ('./tests/inputs/input2.txt')
TEST3 = ('./tests/inputs/input3.txt')


# --------------------------------------------------
def test_exists():
    """Program exists"""
    assert os.path.exists(PRG)

def test_usage() -> None:
    """Print usage"""
    for arg in ['-h', '--help']:
        rv, out = getstatusoutput(f'{RUN} {arg}')
        assert rv == 0
        assert out.lower().startswith('usage:')

def test_dies_no_args() -> None:
    """Dies with no argument"""
    rv, out = getstatusoutput(RUN)
    assert rv != 0
    assert out.lower().startswith('usage:')

def test_arg():
    """Uses command-line arg"""
    for file, expected in [TEST1, TEST2, TEST3]:
        dna = open(file).read()
        retval, out = getstatusoutput(f'{RUN} {dna}')
        assert retval == 0
        assert out == expected
def test_file():
    """Uses file arg"""
    for file, expected in [TEST1, TEST2, TEST3]:
        reval, out = getstatusoutput(f'{RUN} {file}')
        assert retval == 0
        assert out == expected
