################################
# Import Modules Without Error #
################################

import multipy as mp

def main() -> None:
    temp1 = mp.Matrix(8)
    temp2 = mp.Matrix(8)
    alg = mp.Algorithm()
    arg = [temp1, temp2]
    alg.populate(arg)
    print(alg)

if __name__ == "__main__":
    main()
