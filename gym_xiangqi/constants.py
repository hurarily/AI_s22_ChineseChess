"""
This file contains all the constants used throughout
the Xiangqi environment.
"""

""" PATHS """
PATH_TO_SOUNDS = "sounds/"
PATH_TO_BOARD = "images/board/"
PATH_TO_BLACK = "images/black_pieces/"
PATH_TO_RED = "images/red_pieces/"

""" PYGAME """
WINDOW_WIDTH = 521
WINDOW_HEIGHT = 800
FPS = 20
COUNT = 10

""" POINTS """
PIECE_POINTS = [
    0.,                     # EMPTY: No point for empty grid
    100.,                   # GENERAL: Priceless for the general
    2., 2.,                 # ADVISOR: 2.0 points
    2., 2.,                 # ELEPHANT: 2.0 points
    4., 4.,                 # HORSE: 4.0 points
    9., 9.,                 # CHARIOT: 9.0 points
    4.5, 4.5,               # CANNON: 4.5 points
    1., 1., 1., 1., 1.,     # SOLDIER: 1.0 point (2.0 after crossing river)
]

ILLEGAL_MOVE = -10.
WIN = PIECE_POINTS[1]
LOSE = -PIECE_POINTS[1]

""" PIECE """
ALLY = 1
ENEMY = -1

PIECE_CNT = 16              # Total number of pieces in each side

# Piece IDs
EMPTY = 0
GENERAL = 1
ADVISOR_1 = 2
ADVISOR_2 = 3
ELEPHANT_1 = 4
ELEPHANT_2 = 5
HORSE_1 = 6
HORSE_2 = 7
CHARIOT_1 = 8
CHARIOT_2 = 9
CANNON_1 = 10
CANNON_2 = 11
SOLDIER_1 = 12
SOLDIER_2 = 13
SOLDIER_3 = 14
SOLDIER_4 = 15
SOLDIER_5 = 16

PIECE_ID_TO_NAME = [
    "EMPTY", "GENERAL", "ADVISOR_1", "ADVISOR_2",
    "ELEPHANT_1", "ELEPHANT_2", "HORSE_1", "HORSE_2",
    "CHARIOT_1", "CHARIOT_2", "CANNON_1", "CANNON_2",
    "SOLDIER_1", "SOLDIER_2", "SOLDIER_3", "SOLDIER_4", "SOLDIER_5",
]

# Piece Movement Offsets
ORTHOGONAL = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIAGONAL = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
ELEPHANT_MOVE = [(-2, 2), (2, 2), (2, -2), (-2, -2)]
HORSE_MOVE = [
    [(-1, 0), (-1, -1)], [(-1, 0), (-1, 1)],
    [(0, 1), (-1, 1)], [(0, 1), (1, 1)],
    [(1, 0), (1, 1)], [(1, 0), (1, -1)],
    [(0, -1), (1, -1)], [(0, -1), (-1, -1)]
]

# Piece States
RED = 0
BLACK = 1
DEAD = 0
ALIVE = 1

# Piece Size
PIECE_WIDTH = 58
PIECE_HEIGHT = 58
MINI_PIECE_WIDTH = 29
MINI_PIECE_HEIGHT = 29

""" BOARD """
# Board Size
BOARD_WIDTH = 521
BOARD_HEIGHT = 577
BOARD_Y_OFFSET = (WINDOW_HEIGHT/2 - BOARD_HEIGHT/2)

# Board Dimension
BOARD_ROWS = 10
BOARD_COLS = 9

# Palace coordinates
PALACE_ENEMY_ROW = (0, 2)
PALACE_ALLY_ROW = (7, 9)
PALACE_COL = (3, 5)

# River line
RIVER_LOW = 4
RIVER_HIGH = 5

INITIAL_BOARD = [
    [-9, -7, -5, -3, -1, -2, -4, -6, -8],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -11, 0, 0, 0, 0, 0, -10, 0],
    [-16, 0, -15, 0, -14, 0, -13, 0, -12],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [12, 0, 13, 0, 14, 0, 15, 0, 16],
    [0, 10, 0, 0, 0, 0, 0, 11, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [8, 6, 4, 2, 1, 3, 5, 7, 9]
]

""" OTHER """
MAX_REP = 9         # number that is large enough to cover board width/height
TOTAL_POS = BOARD_ROWS * BOARD_COLS
MAX_PERPETUAL_JIANG = 4

""" Piece Coordinate Conversion """
COOR_DELTA = 57
COOR_OFFSET = 5

POINT_BLACK_HORSE = [
    [0, -4, 0, 0, 0, 0, 0, -4, 0],
    [0, 2, 4, 4, -2, 4, 4, 2, 0],
    [4, 2, 8, 8, 4, 8, 8, 2, 4],
    [2, 6, 8, 6, 10, 6, 8, 6, 2],
    [4, 12, 16, 14, 12, 14, 16, 12, 4],
    [6, 16, 14, 18, 16, 18, 14, 16, 6],
    [8, 24, 18, 24, 20, 24, 18, 24, 8],
    [12, 14, 16, 20, 18, 20, 16, 14, 12],
    [4, 10, 28, 16, 8, 16, 28, 10, 4],
    [4, 8, 16, 12, 4, 12, 16, 8, 4]
]

POINT_BLACK_CHARIOT = [
    [-2, 10, 6, 14, 12, 14, 6, 10, -2],
    [8, 4, 8, 16, 8, 16, 8, 4, 8],
    [4, 8, 6, 14, 12, 14, 6, 8, 4],
    [6, 10, 8, 14, 14, 14, 8, 10, 6],
    [12, 16, 14, 20, 20, 20, 14, 16, 12],
    [12, 14, 12, 18, 18, 18, 12, 14, 12],
    [12, 18, 16, 22, 22, 22, 16, 18, 12],
    [12, 12, 12, 18, 18, 18, 12, 12, 12],
    [16, 20, 18, 24, 26, 24, 18, 20, 16],
    [14, 14, 12, 18, 16, 18, 12, 14, 14]
]

POINT_BLACK_CANNON = [
    [0, 0, 2, 6, 6, 6, 2, 0, 0],
    [0, 2, 4, 6, 6, 6, 4, 2, 0],
    [4, 0, 8, 6, 10, 6, 8, 0, 4],
    [0, 0, 0, 2, 4, 2, 0, 0, 0],
    [-2, 0, 4, 2, 6, 2, 4, 0, -2],
    [0, 0, 0, 2, 8, 2, 0, 0, 0],
    [0, 0, -2, 4, 10, 4, -2, 0, 0],
    [2, 2, 0, -10, -8, -10, 0, 2, 2],
    [2, 2, 0, -4, -14, -4, 0, 2, 2],
    [6, 4, 0, -10, -12, -10, 0, 4, 6]
]

POINT_BLACK_SOLDIER = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, -2, 0, 4, 0, -2, 0, 0],
    [2, 0, 8, 0, 8, 0, 8, 0, 2],
    [6, 12, 18, 18, 20, 18, 18, 12, 6],
    [10, 20, 30, 34, 40, 34, 30, 20, 10],
    [14, 26, 42, 60, 80, 60, 42, 26, 14],
    [18, 36, 56, 80, 120, 80, 56, 36, 18],
    [0, 3, 6, 9, 12, 9, 6, 3, 0]
]

POINT_RED_HORSE = [
    [4, 8, 16, 12, 4, 12, 16, 8, 4],
    [4, 10, 28, 16, 8, 16, 28, 10, 4],
    [12, 14, 16, 20, 18, 20, 16, 14, 12],
    [8, 24, 18, 24, 20, 24, 18, 24, 8],
    [6, 16, 14, 18, 16, 18, 14, 16, 6],
    [4, 12, 16, 14, 12, 14, 16, 12, 4],
    [2, 6, 8, 6, 10, 6, 8, 6, 2],
    [4, 2, 8, 8, 4, 8, 8, 2, 4],
    [0, 2, 4, 4, -2, 4, 4, 2, 0],
    [0, -4, 0, 0, 0, 0, 0, -4, 0]
]

POINT_RED_CHARIOT = [
    [14, 14, 12, 18, 16, 18, 12, 14, 14],
    [16, 20, 18, 24, 26, 24, 18, 20, 16],
    [12, 12, 12, 18, 18, 18, 12, 12, 12],
    [12, 18, 16, 22, 22, 22, 16, 18, 12],
    [12, 14, 12, 18, 18, 18, 12, 14, 12],
    [12, 16, 14, 20, 20, 20, 14, 16, 12],
    [6, 10, 8, 14, 14, 14, 8, 10, 6],
    [4, 8, 6, 14, 12, 14, 6, 8, 4],
    [8, 4, 8, 16, 8, 16, 8, 4, 8],
    [-2, 10, 6, 14, 12, 14, 6, 10, -2]
]

POINT_RED_CANNON = [
    [6, 4, 0, -10, -12, -10, 0, 4, 6],
    [2, 2, 0, -4, -14, -4, 0, 2, 2],
    [2, 2, 0, -10, -8, -10, 0, 2, 2],
    [0, 0, -2, 4, 10, 4, -2, 0, 0],
    [0, 0, 0, 2, 8, 2, 0, 0, 0],
    [-2, 0, 4, 2, 6, 2, 4, 0, -2],
    [0, 0, 0, 2, 4, 2, 0, 0, 0],
    [4, 0, 8, 6, 10, 6, 8, 0, 4],
    [0, 2, 4, 6, 6, 6, 4, 2, 0],
    [0, 0, 2, 6, 6, 6, 2, 0, 0]
]

POINT_RED_SOLDIER = [
    [0, 3, 6, 9, 12, 9, 6, 3, 0],
    [18, 36, 56, 80, 120, 80, 56, 36, 18],
    [14, 26, 42, 60, 80, 60, 42, 26, 14],
    [10, 20, 30, 34, 40, 34, 30, 20, 10],
    [6, 12, 18, 18, 20, 18, 18, 12, 6],
    [2, 0, 8, 0, 8, 0, 8, 0, 2],
    [0, 0, -2, 0, 4, 0, -2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]