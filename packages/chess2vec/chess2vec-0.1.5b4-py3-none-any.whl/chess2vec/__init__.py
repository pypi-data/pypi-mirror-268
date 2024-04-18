from typing import Iterable, TextIO

import chess
import chess.pgn
import numpy as np
from tqdm import tqdm

import chess2vec._utils as _u
import chess2vec._utils.sparse as _spu

VEC_SIZE = 5 * 64 * 64


class PositionLoader:
    def __init__(self, with_fen: bool = True) -> None:
        self.actions = _spu.csr_matrix((0, VEC_SIZE), dtype=np.uint8)

        self.with_fen = with_fen

        if self.with_fen:
            self.labels = []

    def _update_labels(self, labels: Iterable[str]):
        if self.with_fen:
            self.labels += labels

    def load_fen(self, x: Iterable[str]):
        builder = _spu.csr_matrix_builder()
        idx = 0

        for fen in x:
            board = chess.Board(fen)

            builder.add_entry(idx, list(_u.actions(board)), 1, np.uint8)

            idx += 1

        self._update_labels(list(x))
        self.actions = _spu.vstack(
            [self.actions, builder.build((idx, VEC_SIZE), np.uint8)]
        )

    def load_pgn(self, x: TextIO, max_games: int = None, status: bool = False):
        if max_games <= 0:
            return

        if max_games is None:
            max_games = float("inf")

        builder = _spu.csr_matrix_builder()
        idx = num_game = 0

        if status:
            bar = tqdm(total=max_games)

        game = chess.pgn.read_game(x)

        while game and num_game < max_games:
            board = game.board()

            builder.add_entry(idx, list(_u.actions(board)), 1, np.uint8)
            self._update_labels([board.fen()])

            idx += 1

            for move in game.mainline_moves():
                board.push(move)

                builder.add_entry(idx, list(_u.actions(board)), 1, np.uint8)
                self._update_labels([board.fen()])

                idx += 1

            if status:
                bar.update(1)

            game = chess.pgn.read_game(x)
            num_game += 1

        self.actions = _spu.vstack(
            [self.actions, builder.build((idx, VEC_SIZE), np.uint8)]
        )

        if status:
            bar.close()

    def load_npz(self, x: Iterable[str]):
        """loads data from .npz file"""
        for file in x:
            with np.load(file) as loaded:
                indices = loaded["mat_indices"]

                mat = _spu.csr_matrix(
                    (
                        np.ones_like(indices, dtype=np.uint8),
                        indices,
                        loaded["mat_indptr"],
                    ),
                    shape=(loaded["size"], VEC_SIZE),
                )

                self.actions = _spu.vstack([self.actions, mat])
                self._update_labels(list(loaded["labels"]))

    def save(self, file: str) -> None:
        """saves the already loaded data to a compressed .npz file."""

        _save_dict = {}
        _save_dict.update(
            mat_indices=self.actions.indices,
            mat_indptr=self.actions.indptr,
            size=self.size,
        )

        if self.with_fen:
            _save_dict.update(labels=self.labels)

        np.savez_compressed(file, **_save_dict)

    @property
    def size(self) -> int:
        return self.actions.shape[0]

    def batched(self, batch_size: int):
        for idx in range(0, self.size, batch_size):
            child = self.__new__(type(self))
            child.__init__(self.with_fen)

            child.actions = self.actions[idx : idx + batch_size]
            child._update_labels(self.labels[idx : idx + batch_size])

            yield child

    def shuffle(self, *, seed: int = 42):
        rng = np.random.default_rng(seed)
        idx = rng.permutation(len(self.actions))

        self.actions = self.actions[idx]

        if self.with_fen:
            self.labels = list(np.array(self.labels)[idx])

    def cov(self) -> np.ndarray:
        return _spu.scov(self.actions.T).toarray()

    def __add__(self, item):
        assert isinstance(item, type(self))

        new = self.__new__(type(self))
        new.__init__(self.with_fen)

        new.actions = _spu.vstack([self.actions, item.actions])

        if self.with_fen:
            new.labels = self.labels + item.labels

        return new

    def __repr__(self):
        return "PositionLoader(size={})".format(self.size)
