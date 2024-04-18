from typing import Iterable, TextIO, Callable

import chess
import chess.pgn
import numpy as np
import scipy.sparse
from alive_progress import alive_bar

import chess2vec._utils.sparse as spu

VEC_BLOCK = 64 * 64
VEC_SIZE = 5 * VEC_BLOCK


from time import perf_counter

def timeit(func: Callable, *args, **kwargs):
    time_start = perf_counter()
    result = func(*args, **kwargs)
    time_end = perf_counter()
    print(f"{func.__name__}: {(time_end - time_start):.8f}")
    return result


class csr_matrix_builder:
    def __init__(self):
        self.data = []
        self.rows = []
        self.columns = []

    def add_entry(self, rows, columns, data=None):
        self.columns += columns
        
        if isinstance(rows, int):
            rows = [rows for _ in range(len(columns))]
        
        self.rows += rows

        if data is None:
            data = [1 for _ in range(len(rows))]

        self.data += data

    def build(self, shape):
        return scipy.sparse.csr_matrix(
            [self.data, (self.rows, self.columns)], shape=shape
        )


def _actions(board: chess.Board):
    for move in board.legal_moves:
        pt = board.piece_type_at(move.from_square)

        if not board.turn:
            move.from_square ^= 0x38
            move.to_square ^= 0x38

        idx = 64 * move.from_square + move.to_square

        match pt:
            case chess.QUEEN:
                yield from (VEC_BLOCK * 2 + idx, VEC_BLOCK * 3 + idx)
            case chess.KING:
                yield VEC_BLOCK * 4 + idx
            case _:
                yield VEC_BLOCK * (pt - 1) + idx


class PositionEncoder:
    def __init__(self) -> None:
        self.positions = []
        self._actions_matrix = scipy.sparse.csr_matrix((0, VEC_SIZE), dtype=np.uint8)

    def _load_indices(self, rows, columns):
        mat = scipy.sparse.csr_matrix(
            (
                np.ones_like(columns, dtype=np.uint8),
                (rows, columns),
            ),
            shape=(int(np.max(rows)) + 1, VEC_SIZE),
        )

        self._actions_matrix = scipy.sparse.vstack([self._actions_matrix, mat])

    def load_fen(self, x: Iterable[str]):
        rows, columns = [], []
        row_idx = 0

        for fen in x:
            board = chess.Board(fen)

            actions = list(_actions(board))
            columns += actions
            rows += [row_idx for _ in range(len(actions))]

            row_idx += 1

        self._load_indices(rows, columns)
        self.positions += list(x)

    def load_pgn(self, x: TextIO, max_games: int = None):
        if max_games <= 0:
            return

        if max_games is None:
            max_games = float("inf")
            
        builder = csr_matrix_builder()
        positions = []
        idx = num_game = 0
        
        with alive_bar() as bar:
            game = chess.pgn.read_game(x)

            while game and num_game < max_games:                    
                board = game.board()

                builder.add_entry(idx, list(_actions(board)))
                positions.append(board.fen())
                
                idx += 1
                bar()

                for move in game.mainline_moves():
                    board.push(move)

                    builder.add_entry(idx, list(_actions(board)))
                    positions.append(board.fen())
                    
                    idx += 1
                    bar()

                game = chess.pgn.read_game(x)
                num_game += 1
                    
        self._actions_matrix = scipy.sparse.vstack([self._actions_matrix, builder.build((idx, VEC_SIZE))])
        self.positions += positions

    def load_npz(self, x: Iterable[str]):
        for file in x:
            with np.load(file) as loaded:
                indices = loaded["mat_indices"]
                mat = scipy.sparse.csr_matrix(
                    (
                        np.ones_like(indices, dtype=np.uint8),
                        indices,
                        loaded["mat_indptr"],
                    ),
                    shape=(loaded["size"], VEC_SIZE),
                )

                positions = list(loaded["positions"])

            self._actions_matrix = scipy.sparse.vstack([self._actions_matrix, mat])
            self.positions += positions

    def save(self, file) -> None:
        np.savez_compressed(
            file,
            mat_indices=self._actions_matrix.indices,
            mat_indptr=self._actions_matrix.indptr,
            size=self.size,
            positions=self.positions,
        )

    @property
    def size(self) -> int:
        return self._actions_matrix.shape[0]

    def batched(self, batch_size: int = None):
        if batch_size is None:
            batch_size = self.size

        for idx in range(0, self.size, batch_size):
            child = self.__new__(type(self))
            child._actions_matrix = self._actions_matrix[idx : idx + batch_size]
            child.positions = self.positions[idx : idx + batch_size]

            yield child

    def shuffle(self, *, seed: int = 42):
        rng = np.random.default_rng(seed)
        idx = rng.permutation(len(self._actions_matrix))

        self._actions_matrix = self._actions_matrix[idx]
        self.positions = list(np.array(self.positions)[idx])

    def cov(self) -> np.ndarray:
        return spu.cov(self._actions_matrix.T).toarray()

    def encode(self) -> np.ndarray: ...

    def __add__(self, item):
        assert isinstance(item, type(self))

        new = self.__new__(type(self))
        new._actions_matrix = scipy.sparse.vstack(
            [self._actions_matrix, item._actions_matrix]
        )
        new.positions = self.positions + item.positions

        return new

    def __repr__(self):
        return "PositionEncoder(size={})".format(self.size)
