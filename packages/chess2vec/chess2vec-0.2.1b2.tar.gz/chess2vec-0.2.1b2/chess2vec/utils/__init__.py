import chess


def yield_actions(board: chess.Board):
    for move in board.legal_moves:
        pt = board.piece_type_at(move.from_square)

        if not board.turn:
            move.from_square ^= 0x38
            move.to_square ^= 0x38

        yield 64 * (64 * pt + move.from_square) + move.to_square


def yield_pieces(board: chess.Board):
    for sq in chess.scan_reversed(board.occupied):
        piece = board.piece_at(sq)

        if not board.turn:
            sq ^= 0x38

        yield 64 * (6 * (int(board.turn) ^ piece.color) + piece.piece_type) + sq
