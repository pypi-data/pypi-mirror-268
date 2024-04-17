import numpy as np


def norm_l2(a: np.ndarray) -> np.ndarray:
    """compute the l2 norm of a batch of vectors."""
    assert a.ndim == 2
    return np.sqrt(np.sum(a**2, axis=1))


def distance_l2(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """compute the l2 (euclidean distance) between two batches of vectors."""
    return norm_l2(a - b)


def cosine(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """compute the cosine similarity between two batches of vectors."""
    return np.sum(a * b, axis=1) / (norm_l2(a) * norm_l2(b))
