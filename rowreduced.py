import numpy


def rreform(matrx):
    """ I want to return the row reduced echelon form of the given matrix. """

    row, col = matrx.shape
    if row == 0 or col == 0:
        return matrx

    for n in range(len(matrx)):
        if matrx[n, 0] != 0:
            break

    else:
        rref_matrix = rreform(matrx[:, 1:])
        return numpy.hstack([matrx[:, :1], rref_matrix])

    if n > 0:
        nth_row = matrx[n].copy()
        matrx[n] = matrx[0]
        matrx[0] = nth_row

    matrx[0] = matrx[0] / matrx[0, 0]
    matrx[1:] -= matrx[0] * matrx[1:, 0:1]

    rref_matrix = rreform(matrx[1:, 1:])

    return numpy.vstack([matrx[:1], numpy.hstack([matrx[1:, :1], rref_matrix])])
