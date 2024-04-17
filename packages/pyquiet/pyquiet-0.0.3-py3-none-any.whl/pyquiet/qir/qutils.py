import numpy as np
import math


def gen_np_square_matrix(matrix: list):
    if 4 ** math.log(len(matrix), 4) != len(matrix) or len(matrix) == 0:
        return np.array(matrix)
    size = int(math.log(len(matrix), 2))
    new_matrix = [matrix[i : i + size] for i in range(0, len(matrix), size)]
    return np.array(new_matrix)
