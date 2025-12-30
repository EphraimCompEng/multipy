###################################
# Generate Multiplier Truth Table #
###################################




"""
Do not optimise generation until functionality is actually tested for
edge cases and speed. Then refactor by using appropriate patterns,
simplification, etc., before applying multiprocessing and beyond.

"""




from _typeshed import GenericPath
import multipy as mp
import pathlib
import itertools


def truth_scope(domain: tuple, range: tuple=(0,-1)) -> combinations:
    """
    Generate a generator based on the domain and range of a desired truth table
    >>> domain = (min_input, max_input)
    >>> range  = (min_output, max_output)

    Use '-1' for no upper bound
    """

    scope =
