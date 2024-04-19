from typing import TextIO

import chess.pgn


def skip(pgn: TextIO, n_games: int):
    """skips `n_games` of `pgn`"""
    num_game = 0

    while num_game < n_games:
        game = chess.pgn.read_game(pgn)

        if not game:
            return False

        num_game += 1

    return True
