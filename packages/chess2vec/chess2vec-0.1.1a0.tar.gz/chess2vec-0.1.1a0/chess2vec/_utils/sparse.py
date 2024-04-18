from typing import Callable

import numpy as np
from scipy.sparse import csr_matrix


def apply(
    mat: csr_matrix, f: Callable[[np.ndarray], np.ndarray], *, axis: int = 0
) -> csr_matrix:
    assert axis in (0, 1)

    if axis == 0:
        mat.data = f(mat.data)

    elif axis == 1:
        for row_start, row_end in zip(mat.indptr[:-1], mat.indptr[1:]):
            if row_end > row_start:
                mat.data[row_start:row_end] = f(mat.data[row_start:row_end])

    return mat


def cov(mat: csr_matrix) -> csr_matrix:
    mat = apply(mat, lambda x: x - x.sum() / mat.shape[1], axis=1)
    return mat @ mat.T


def shuffled(mat: csr_matrix, rng: np.random.Generator):
    idx = rng.permutation(mat.shape[0])
    return mat[idx]
