###################################
# Generate Multiplier Truth Table #
###################################


from collections.abc import Generator

from .algorithm import Algorithm



"""
Do not optimise generation until functionality is actually tested for
edge cases and speed. Then refactor by using appropriate patterns,
simplification, etc., before applying multiprocessing and beyond.

"""


def truth_scope(domain_: tuple[int,int], range_: tuple[int,int]) -> Generator:
    """
    A generator based on the domain and range of a desired truth table.
    >>> domain = (min_in, max_in)
    >>> range  = (min_out, max_out)
    Yields: (operand_a, operand_b)
    """

    min_in, max_in = domain_
    min_out, max_out = range_
    if min_in <= 0 or min_out <= 0:
        raise ValueError("Minimum input and output values must be greater than zero.")
    if min_in > max_in:
        raise ValueError("Minimum input value greater than maximum input value.")
    if min_out > max_out:
        raise ValueError("Minimum output greater than maximum output value.")

    # Efficient calculation of possible input values via internet:
    # for x < a * b < y use x/b < a < y/b to find limits of 'a', for a fixed 'b'

    gen1 = (b for b in range(min_in, max_in + 1))
    for b in gen1:
        limit_mn_b = (min_out // b) if min_out < (min_out // b) else min_in
        limit_mx_b = (max_out // b) if (max_out // b) < max_in else max_in
        gen2 = (a for a in range(limit_mn_b, limit_mx_b+1))
        for a in gen2:
            yield a, b # BUG -- b needs stricter limits

def shallow_truth_table(scope: Generator, alg: Algorithm) -> Generator:
    print(alg.bits)
    return (Algorithm.build_matrix(a, b, alg.bits) for a, b in scope)


def truth_table(scope: Generator, alg: Algorithm) -> Generator:
    """
    A generator which yields all stages of an algorithm for a given
    set of operands a, b.
    """
    ...
