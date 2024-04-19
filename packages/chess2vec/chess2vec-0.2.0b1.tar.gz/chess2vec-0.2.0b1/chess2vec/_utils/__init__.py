import chess
from collections import defaultdict


def square_pool(sq, pool_size):
    return (((sq >> 3) // pool_size) * (8 // pool_size)) | ((sq & 7) // pool_size)


def actions(board: chess.Board, pool_size=1):
    a = defaultdict(lambda: 0)
    
    for move in board.legal_moves:
        pt = board.piece_type_at(move.from_square)

        if not board.turn:
            move.from_square ^= 0x38
            move.to_square ^= 0x38

        idx = (8 // pool_size) ** 2 * square_pool(
            move.from_square, pool_size
        ) + square_pool(move.to_square, pool_size)
        
        plane = (8 // pool_size) ** 4

        match pt:
            case chess.QUEEN:
                a[2 * plane + idx] += 1
                a[3 * plane + idx] += 1
            case chess.KING:
                a[4 * plane + idx] += 1
            case _:
                a[(pt - 1) * plane + idx] += 1
    
    return a.keys(), a.values()
