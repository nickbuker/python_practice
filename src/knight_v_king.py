def knightVsKing(kt_pos, kg_pos):
    board = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
    kt, kg = (kt_pos[0], board[kt_pos[1]]), (kg_pos[0], board[kg_pos[1]])
    kt_moves = find_moves(kt, kg, "knight")
    if check_kill(kt_moves, kg):
        return "Knight"
    kg_moves = find_moves(kt, kg, "king")
    if check_kill(kg_moves, kt):
        return "King"
    return "None"


def find_moves(kt, kg, piece):
    if piece == "knight":
        kt_moves = [(kt[0] + 2, kt[1] + 1), (kt[0] + 2, kt[1] - 1), (kt[0] + 1, kt[1] + 2),
                    (kt[0] - 1, kt[1] + 2), (kt[0] - 2, kt[1] + 1), (kt[0] - 2, kt[1] - 1),
                    (kt[0] + 1, kt[1] - 2), (kt[0] - 1, kt[1] - 2)]
        return filter_moves(kt_moves)
    if piece == "king":
        kg_moves = [(kg[0] + 1, kg[1]), (kg[0] - 1, kg[1]), (kg[0], kg[1] + 1),
                    (kg[0], kg[1] - 1), (kg[0] + 1, kg[1] + 1), (kg[0] - 1, kg[1] - 1),
                    (kg[0] + 1, kg[1] - 1), (kg[0] - 1, kg[1] + 1)]
        return filter_moves(kg_moves)


def filter_moves(moves):
    new_moves = []
    for move in moves:
        if move[0] > 0 and move[0] < 9 and move[1] > 0 and move[1] < 9:
            new_moves.append(move)
    return new_moves


def check_kill(moves, pos):
    return pos in moves
