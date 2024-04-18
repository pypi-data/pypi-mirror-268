from typing import Callable, Iterable

import numpy as np
from scipy.sparse import csr_matrix, vstack


class csr_matrix_builder:
    def __init__(self):
        self.data = []
        self.rows = []
        self.columns = []

    def add_entry(
        self,
        rows: int | Iterable[int],
        columns: Iterable[int],
        data: int | Iterable[int] = 1,
        dtype=np.float32,
    ):
        size = len(columns)

        if isinstance(rows, int):
            rows = [rows for _ in range(size)]

        self.rows += rows
        self.columns += columns

        if isinstance(data, int):
            data = [data for _ in range(size)]

        self.data += list(map(dtype, data))

    def build(self, shape, dtype=np.float32):
        return csr_matrix(
            (self.data, (self.rows, self.columns)), shape=shape, dtype=dtype
        )


def apply(
    mat: csr_matrix, f: Callable[[np.ndarray], np.ndarray], *, axis: int = 0
) -> csr_matrix:
    """applies the function `f` to `mat.data` along the specified axis (default 0)."""
    assert axis in (0, 1)

    if axis == 0:
        mat.data = f(mat.data)

    elif axis == 1:
        for row_start, row_end in zip(mat.indptr[:-1], mat.indptr[1:]):
            if row_end > row_start:
                mat.data[row_start:row_end] = f(mat.data[row_start:row_end])

    return mat


def scov(mat: csr_matrix) -> csr_matrix:
    """computes sparse covariance of `mat` (covariance of non-zero entries)."""
    # TODO try updating to handle all entries
    mat = apply(mat, lambda x: x - x.sum() / mat.shape[1], axis=1)
    return mat @ mat.T


def shuffled(mat: csr_matrix, rng: np.random.Generator):
    idx = rng.permutation(mat.shape[0])
    return mat[idx]
