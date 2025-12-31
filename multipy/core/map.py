##################################
# Map, Swap Bits Inside A Matrix #
##################################




###
# Simple maps move entire rows
###
#
# import multipy as mp
from typing import Any


def build_map(
) -> list[list[int]]:
    """
    A map matrix holds signed hexadecimal numbers representing a vertical
    offset for a given bit when applied to an algorithm.

    [map]\t   [matrix]\t[effect]\n
    00 02 01\t _ 0 1\t  _ 1 _\n
    00 FF 00\t 0 1 _\t  0 _ 1\n
    00 00 00\t _ _ _\t  _ 0 _\n
    """
    ...

def dadda_map():
    """
    Return map to collect partial products into an upside down triangle:
    a prerequisite for the dadda algorithm.
    """
    ...

def build_simple_map():
    """
    """
    ...
