#################################################
# Generating, Aligning Initial Partial Products #
#################################################

# import multipy as mp
from typing import Any


class Matrix:
    def __init__(self, bits: int):
        valid_range = {4, 8}
        if bits in valid_range:
            self.bits = bits
        else:
            raise ValueError(f"Valid bit lengths: {valid_range}")
        self.matrix = self.__build_matrix()

    def __build_matrix(self) -> list[list[int]]:
        """
        Build a logic AND matrix for a bitwidth of self.bits. For example:
        >>> self.bits = 4
        >>> build_matrix()
        [['_','_','_','_',0,0,0,0],
         ['_','_','_',0,0,0,0,'_'],
         ['_','_',0,0,0,0,'_','_'],
         ['_',0,0,0,0,'_','_','_']]
        """
        row = [0]*self.bits
        matrix = []
        for i in range(self.bits):
            matrix.append(["_"]*(self.bits-i) + row + ["_"]*i)
        return matrix

    def pprint_matrix(self, matrix: list[list[int]]) -> str:
        """
        Format self.matrix as a string:

        "____0000\n
         ___0000_\n
         __0000__\n
         _0000___"
        """
        pretty = ""
        for i in matrix:
            row = [str(x) for x in i]
            pretty += "".join(row) + "\n"
        return pretty

    def __repr__(self) -> str:
        return self.pprint_matrix(self.matrix)

    def __str__(self) -> str:
        return self.__repr__()

    def __len__(self) -> int:
        return self.bits

    def __getitem__(self, index: int) -> list:
        return self.matrix[index]

    def __eq__(self, matrix: Any, /) -> bool:
        if matrix.bits != self.bits:
            return False
        for i in range(self.bits):
            if matrix[i] != self.matrix[i]:
                return False
        return True
