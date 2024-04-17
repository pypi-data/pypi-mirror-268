from typing import Iterable

import chess
import chess.pgn
import numpy as np
import scipy.sparse

import chess2vec._utils.sparse as spu

VEC_BLOCK = 64 * 64
VEC_SIZE = 5 * VEC_BLOCK


class PositionEncoder:
    def __init__(self) -> None:
        self.positions = []
        self._actions_matrix = scipy.sparse.csr_matrix((0, VEC_SIZE), dtype=np.uint8)

    def load_fen(self, x: Iterable[str]):
        rows, columns = [], []
        row_idx = 0

        for fen in x:
            board = chess.Board(fen)

            for move in board.legal_moves:
                pt = board.piece_type_at(move.from_square)

                if not board.turn:
                    move.from_square ^= 0x38
                    move.to_square ^= 0x38

                idx = 64 * move.from_square + move.to_square

                match pt:
                    case chess.QUEEN:
                        columns += [VEC_BLOCK * 2 + idx, VEC_BLOCK * 3 + idx]
                    case chess.KING:
                        columns += [VEC_BLOCK * 4 + idx]
                    case _:
                        columns += [VEC_BLOCK * (pt - 1) + idx]

                rows.append(row_idx)

            row_idx += 1

        mat = scipy.sparse.csr_matrix(
            (
                np.ones_like(columns, dtype=np.uint8),
                (rows, columns),
            ),
            shape=(1, VEC_SIZE),
        )

        self._actions_matrix = scipy.sparse.vstack([self._actions_matrix, mat])
        self.positions += list(x)

    def load_pgn(self, x: Iterable[str]):
        for file in x:
            with open(file) as pgn:
                game = chess.pgn.read_game(pgn)

                while game:
                    board = game.board()
                    pos = [board.fen()] + [
                        board.push(move) or board.fen()
                        for move in game.mainline_moves()
                    ]
                    self.load_fen(pos)

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
                    shape=(-1, VEC_SIZE),
                )

                positions = list(loaded["positions"])

            self._actions_matrix = scipy.sparse.vstack([self._actions_matrix, mat])
            self.positions += positions

    def save_npz(self, file) -> None:
        np.savez_compressed(
            file,
            mat_indices=self._actions_matrix.indices,
            mat_indptr=self._actions_matrix.indptr,
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
