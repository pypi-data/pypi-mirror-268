import itertools
from typing import Iterable, Literal, TextIO

import chess
import chess.pgn
import numpy as np
from tqdm import tqdm

from chess2vec import utils
from chess2vec.utils import sparse


class PositionLoader:
    def __init__(self, *, with_fen=False, rep: Literal["piece", "action"] = "piece"):
        self.rep = rep

        if self.rep == "piece":
            self.entries = sparse.csr_matrix((0,), dtype=np.uint8)
            self._entries_getter = utils.yield_pieces
            self.entry_size = 2 * 6 * 64

        elif self.rep == "action":
            self.entries = sparse.csr_matrix((0, 6 * 64 * 64), dtype=np.uint8)
            self._entries_getter = utils.yield_actions
            self.entry_size = 6 * 64 * 64

        else:
            raise TypeError

        self.with_fen = with_fen
        if self.with_fen:
            self.labels = []

    def _update_labels(self, labels: Iterable[str]):
        if self.with_fen:
            self.labels += labels

    def load_pgn(self, x: TextIO, max_games: int = None, status: bool = False):
        if max_games is None:
            max_games = float("inf")

        builder = sparse.csr_matrix_builder()
        idx = num_game = 0

        if status:
            bar = tqdm(total=max_games)

        game = chess.pgn.read_game(x)

        while game and num_game < max_games:
            board = game.board()

            for move in itertools.chain(game.mainline_moves(), [chess.Move.null()]):
                entries = list(self._entries_getter(board))
                builder.add_entry(idx, entries, 1, np.uint8)
                self._update_labels([board.fen()])

                board.push(move)
                idx += 1

            if status:
                bar.update(1)

            game = chess.pgn.read_game(x)
            num_game += 1

        self.entries = sparse.vstack(
            [self.entries, builder.build((idx, self.entry_size), np.uint8)]
        )

        if status:
            bar.close()

    def load_npz(self, x: Iterable[str]):
        """loads data from .npz file"""
        for file in x:
            with np.load(file) as loaded:
                indices = loaded["mat_indices"]

                mat = sparse.csr_matrix(
                    (
                        np.ones_like(indices, dtype=np.uint8),
                        indices,
                        loaded["mat_indptr"],
                    ),
                    shape=(loaded["size"], self.entry_size),
                )

                self.entries = sparse.vstack([self.entries, mat])
                self._update_labels(list(loaded["labels"]))

    def save(self, file: str) -> None:
        """saves the already loaded data to a compressed .npz file."""

        _save_dict = {}
        _save_dict.update(
            mat_indices=self.entries.indices,
            mat_indptr=self.entries.indptr,
            size=self.size,
        )

        if self.with_fen:
            _save_dict.update(labels=self.labels)

        np.savez_compressed(file, **_save_dict)

    @property
    def size(self) -> int:
        return self.entries.shape[0]

    def batched(self, batch_size: int):
        for idx in range(0, self.size, batch_size):
            child = self.__new__(type(self))
            child.__init__(self.with_fen)

            child.entries = self.entries[idx : idx + batch_size]
            child._update_labels(self.labels[idx : idx + batch_size])

            yield child

    def shuffle(self, *, seed: int = 42):
        rng = np.random.default_rng(seed)
        idx = rng.permutation(len(self.entries))

        self.entries = self.entries[idx]

        if self.with_fen:
            self.labels = list(np.array(self.labels)[idx])

    def cov(self) -> np.ndarray:
        return sparse.covs(self.entries.T).toarray()

    def __add__(self, item):
        assert isinstance(item, type(self))

        new = self.__new__(type(self))
        new.__init__(self.with_fen)

        new.entries = sparse.vstack([self.entries, item.entries])

        if self.with_fen:
            new.labels = self.labels + item.labels

        return new

    def __repr__(self):
        return "PositionLoader(size={})".format(self.size)
