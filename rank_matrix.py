import sympy


def rank_matrix(matrx: list) -> int:
    """Want to determine the rank of a matrix"""

    # Row reducing our given matrix
    rref_matrx = sympy.Matrix(matrx).rref()
    return len(rref_matrx[-1])
