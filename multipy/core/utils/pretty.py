import multipy as mp

def pprint(matrix: mp.Matrix) -> None:
    """Print formatted Matrix object"""
    pretty_ = mp.Matrix.pretty(matrix)
    print(pretty_)
