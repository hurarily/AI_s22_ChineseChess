from gym_xiangqi.constants import (
    TOTAL_POS,
    POINT_BLACK_HORSE, POINT_BLACK_CHARIOT, POINT_BLACK_CANNON, POINT_BLACK_SOLDIER,
    POINT_RED_HORSE, POINT_RED_CHARIOT, POINT_RED_CANNON, POINT_RED_SOLDIER)


def move_to_action_space(piece_id, start, end):
    """
    The action space is a 1D flat array. We can convert piece id,
    start position and end position to a corresponding index value
    in the action space.

    Parameters:
        piece_id (int): a piece ID integer
        start (tuple(int)): (row, col) start coordinate
        end (tuple(int)): (row, col) end coordinate
    Return:
        Index within the self.possible_actions
    """
    piece_id_val = (piece_id - 1) * pow(TOTAL_POS, 2)
    start_val = (start[0] * 9 + start[1]) * TOTAL_POS
    end_val = end[0] * 9 + end[1]
    return piece_id_val + start_val + end_val


def action_space_to_move(action):
    """
    This is exact opposite of move_to_action_space() method.
    With index value, we can convert this back to piece id,
    start position and end position values.

    Parameters:
        action (int): index value within action space
    Return:
        piece ID, start coordinate, end coordinate
    """
    piece_id, r = divmod(action, pow(TOTAL_POS, 2))
    start_val, end_val = divmod(r, TOTAL_POS)
    start = [0, 0]
    end = [0, 0]
    start[0], start[1] = divmod(start_val, 9)
    end[0], end[1] = divmod(end_val, 9)
    return piece_id + 1, start, end


def is_ally(piece_id):
    """
    Determines if given input piece_id is ally or enemy piece
    This function CANNOT guarantee if the piece is an enemy piece

    Parameters:
        piece_id (int): a piece ID integer
    Return:
        True: given piece ID is an ally piece
        False: given piece ID is either an empty space or an enemy piece
    """
    return piece_id > 0

def evaluate_b(state):
    point = 0
    for x in range(10):
        for y in range(9):
            if state[x][y] == 0:
                continue
            elif state[x][y] == -1:
                point += 100000
            elif state[x][y] == -2 or state[x][y] == -3 or state[x][y] == -4 or state[x][y] == -5:
                point += 120
            elif state[x][y] == -6 or state[x][y] == -7:
                point += 240 + POINT_BLACK_HORSE[x][y]
            elif state[x][y] == -8 or state[x][y] == -9:
                point += 540 + POINT_BLACK_CHARIOT[x][y]
            elif state[x][y] == -10 or state[x][y] == -11:
                point += 270 + POINT_BLACK_CANNON[x][y]
            elif state[x][y] == -12 or state[x][y] == -13 or state[x][y] == -14 or state[x][y] == -15 or state[x][y] == -16:
                if x < 5:
                    point += 60 + POINT_BLACK_SOLDIER[x][y]
                else:
                    point += 120 + POINT_BLACK_SOLDIER[x][y]
            elif state[x][y] == 1:
                point -= 100000
            elif state[x][y] == 2 or state[x][y] == 3 or state[x][y] == 4 or state[x][y] == 5:
                point -= 120
            elif state[x][y] == 6 or state[x][y] == 7:
                point -= 240 + POINT_RED_HORSE[x][y]
            elif state[x][y] == 8 or state[x][y] == 9:
                point -= 540 + POINT_RED_CHARIOT[x][y]
            elif state[x][y] == 10 or state[x][y] == 11:
                point -= 270 + POINT_RED_CANNON[x][y]
            elif state[x][y] == 12 or state[x][y] == 13 or state[x][y] == 14 or state[x][y] == 15 or state[x][y] == 16:
                if x < 5:
                    point -= 60 + POINT_RED_SOLDIER[x][y]
                else:
                    point -= 120 + POINT_RED_SOLDIER[x][y]

    return point
