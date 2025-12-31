################################################
# Returns Template Objects Using User Patterns #
################################################

"""
Simple templates should be represented as a list with each element on
a new line, this makes it clear how each layer is reduced:
>>> my_simple_template = [
    1,
    1,
    2,
    2,
    2,
    .
    .
    .
]

The "run" of a given element determines where adders, run=2, or a
combination of CSAs and HAs, run=3, are used. Elements can be
int or strings, as long as they follow the "run" principle.

Complex templates require a more rigorous approach.

"""


from typing import Any
import string
import copy
import multipy as mp


class Template:
    cell = (ch for ch in string.ascii_lowercase)

    def __init__(self, pattern: list[Any]): # Complex or simple
        valid_range = mp.SUPPORTED_BITWIDTHS
        if len(pattern) not in valid_range:
            raise ValueError(f"Valid bit lengths: {valid_range}")
        if '_' in set(pattern):
            raise ValueError("Invalid pattern: '_' is not allowed")
        self.len   = len(pattern)
        self.pattern  = pattern
        self.template = build_simple_template(self.pattern)
        self.result   = None
    

    
def build_simple_template(pattern: list[str]
) -> list[list[str]]:
    """
    Build a simple template for a given bitwidth.
    >>> self.bits = 4
    >>> build_template(self.pattern)
    [['_','_','_','_','a','a','a','a'], # p = ['a',
        ['_','_','_','a','a','a','a','_'], #      'a',
        ['_','_','b','b','b','b','_','_'], #      'b',
        ['_','b','b','b','b','_','_','_']] #      'b',]
    """
    matrix = []

    return matrix

# Defining a new Template type for list[list[Any]] would be useful?

def build_csa(
    char: str, template_slice: list[list[Any]]
) -> tuple[list, list]: # Carry Save Adder -> (template, result)
    """
    Returns template "slices" for a csa reduction and the resulting slice.\n
    [slice]\t[csa]\t\t[result]\n
    ____0000 ____AaAa         \n
    ___0000_ ___aAaA_ __AaAaAa\n
    __0000__ __AaAa__ __aAaA__\n
    """
    if len(template_slice) != 3:
        raise ValueError("Invalid template slice: must be 3 rows")
    n = len(template_slice[0])
    result = [['_']*n, ['_']*n]
    csa_slice = copy.copy(template_slice)
    tff = char == char.lower() # Toggle flip flop
    for i in range(n):
        # column = [csa_slice[0][i],csa_slice[1][i],csa_slice[2][i]]
        # replace non filler elements with template char
        csa_slice[0][i] = char if (y0:=csa_slice[0][i] != '_') else '_'
        csa_slice[1][i] = char if (y1:=csa_slice[1][i] != '_') else '_'
        csa_slice[2][i] = char if (y2:=csa_slice[2][i] != '_') else '_'
        result[0][i]    = char if 1 <= (y0+y1+y2) else '_'
        result[1][i-1]  = char if 1 < (y0+y1+y2) else '_'
        tff  = not(tff) # True -> False -> True...
        char = char.lower() if tff else char.upper()
    return csa_slice, result


def build_adder(
    char: str, template_slice: list[list[Any]]
) -> tuple[list, list]: # Carry Save Adder -> (template, result)
    """
    Returns template "slices" for addition and the resulting slice.\n
    [slice ]\t[adder]\t[result]\n
    ___0000_ ___aAaA_\n
    __0000__ __AaAa__ _aAaAaA_\n
    """
    if len(template_slice) != 2:
        raise ValueError("Invalid template slice: must be 2 rows")
    n = len(template_slice[0])
    result = [['_']*n]
    adder_slice = copy.copy(template_slice)
    tff = char == char.lower() # Toggle flip flop
    for i in range(n):
        adder_slice[0][i] = char if (y0:=adder_slice[0][i] != '_') else '_'
        adder_slice[1][i] = char if (y1:=adder_slice[1][i] != '_') else '_'
        result[0][i] = char if y0 or y1 else '_'
        tff  = not(tff) # True -> False -> True...
        char = char.lower() if tff else char.upper()

    # Adding final carry
    pre_char = char
    tff  = not(tff) # Undo last flip to find lasr used tff value
    char = char.lower() if tff else char.upper()
    index = result[0].index(char)-1 # find first instance of char - 1
    result[0][index] = pre_char # Final carry place in result template


    return adder_slice, result

###
# Simple laps move entire rows  
###

# def build_map(char: str, matrix: list[list[Any]]
# ) -> list[list[int]]:
#     """
#     A map matrix holds signed hexadecimal numbers representing a vertical
#     offset for a given bit when applied to an algorithm.

#     [map]\t   [matrix]\t[effect]\n
#     00 02 01\t _ 0 1\t  _ 1 _\n
#     00 FF 00\t 0 1 _\t  0 _ 1\n
#     00 00 00\t _ _ _\t  _ 0 _\n
#     """
    
    
#     ...










"""
Complex templates implement decoders and bit-mapping.

Decoders reduce 4 or more bits at a time.

Bit mapping allows for outlining where bits are placed in each stage,
enabling complex implementations and possible optimisations.
"""
