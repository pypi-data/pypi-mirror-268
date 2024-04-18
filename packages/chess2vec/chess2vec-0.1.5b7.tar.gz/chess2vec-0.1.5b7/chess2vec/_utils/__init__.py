import chess


def actions(board: chess.Board):
    """yields all actions on the `board`."""
    for move in board.legal_moves:
        pt = board.piece_type_at(move.from_square)

        if not board.turn:
            move.from_square ^= 0x38
            move.to_square ^= 0x38

        idx = 64 * move.from_square + move.to_square

        match pt:
            case chess.QUEEN:
                yield from (64 * 64 * 2 + idx, 64 * 64 * 3 + idx)
            case chess.KING:
                yield 64 * 64 * 4 + idx
            case _:
                yield 64 * 64 * (pt - 1) + idx
