from re import S
import numpy as np
import random

from gym_xiangqi.constants import (ALLY, BLACK, EMPTY, DEAD, PIECE_POINTS)
from gym_xiangqi.utils import (action_space_to_move, evaluate_b)
from gym_xiangqi.piece import (
    General, Advisor, Elephant, Horse, Chariot, Cannon, Soldier
)

class AlphaBetaAgent:
    """
    This is the implementation of the simplest
    agent possible to play the game of Xiang Qi.
    The agent will simply choose a random move
    out of all the possible moves and return that.
    """
    def __init__(self):
        self.st = None
        self.m = 0
        self.moves = {}
        self.cnt = 0

    def alphabeta(self, st, turn, depth, a, b):
        self.cnt = self.cnt + 1
        if depth == 0:
            return evaluate_b(st)
        self.moves[depth] = []
        self.moves[depth] = self.gen_move(st, turn)
        mini, maxi = 1000000, -1000000
        val = 0
        for i in range(len(self.moves[depth])):
            piece, start, end = self.moves[depth][i]
            st[start[0]][start[1]] = EMPTY
            tmp = st[end[0]][end[1]]
            st[end[0]][end[1]] = piece
            # print(piece, start, end, depth)
            val = self.alphabeta(st, -1*turn, depth-1, a, b)
            # print(piece, start, end, val, a, b, depth)
            st[start[0]][start[1]] = piece
            st[end[0]][end[1]] = tmp
            if turn == -1:
                mini = min(mini, val)
                b = min(b, mini)
                if a > b:
                    break
            elif turn == 1:
                maxi = max(maxi, val)
                if maxi > a:
                    a = maxi
                    if depth == 3:
                        self.m = i
                    if a > b:
                        break
        
        if turn == 1:
            return maxi
        elif turn == -1:
            return mini
    
    def move(self, env):
        """
        Make a random move based on the environment.
        """
        self.cnt = 0
        self.alphabeta(env.state, 1, 3, -1000000, 1000000)
        print("number of iterations: %d" % self.cnt)
        return self.m
    
    def gen_move(self, board, turn):
        moves = []
        if turn == 1:
            for x in range(10):
                for y in range(9):
                    if board[x][y] == -12 or board[x][y] == -13 or board[x][y] == -14 or board[x][y] == -15 or board[x][y] == -16:
                        if self.moveable(board, board[x][y], x, y, x+1, y, turn):
                            moves.append((board[x][y], [x,y], [x+1,y]))
                        if self.moveable(board, board[x][y], x, y, x, y-1, turn):
                            moves.append((board[x][y], [x,y], [x,y-1]))
                        if self.moveable(board, board[x][y], x, y, x, y+1, turn):
                            moves.append((board[x][y], [x,y], [x,y+1]))
                    if board[x][y] == -10 or board[x][y] == -11:
                        for i in range(10):
                            if self.moveable(board,board[x][y],x,y,i,y,turn):
                                moves.append((board[x][y], [x,y], [i,y]))
                        for i in range(9):
                            if self.moveable(board,board[x][y],x,y,x,i,turn):
                                moves.append((board[x][y], [x,y], [x,i]))
                    if board[x][y] == -8 or board[x][y] == -9:
                        for i in range(10):
                            if self.moveable(board,board[x][y],x,y,i,y,turn):
                                moves.append((board[x][y], [x,y], [i,y]))
                        for i in range(9):
                            if self.moveable(board,board[x][y],x,y,x,i,turn):
                                moves.append((board[x][y], [x,y], [x,i]))
                    if board[x][y] == -6 or board[x][y] == -7:
                        if self.moveable(board,board[x][y],x,y,x+1,y-2,turn):
                            moves.append((board[x][y], [x,y], [x+1,y-2]))
                        if self.moveable(board,board[x][y],x,y,x-1,y-2,turn):
                            moves.append((board[x][y], [x,y], [x-1,y-2]))
                        if self.moveable(board,board[x][y],x,y,x-1,y+2,turn):
                            moves.append((board[x][y], [x,y], [x-1,y+2]))
                        if self.moveable(board,board[x][y],x,y,x+1,y+2,turn):
                            moves.append((board[x][y], [x,y], [x+1,y+2]))
                        if self.moveable(board,board[x][y],x,y,x-2,y+1,turn):
                            moves.append((board[x][y], [x,y], [x-2,y+1]))
                        if self.moveable(board,board[x][y],x,y,x-2,y-1,turn):
                            moves.append((board[x][y], [x,y], [x-2,y-1]))
                        if self.moveable(board,board[x][y],x,y,x+2,y-1,turn):
                            moves.append((board[x][y], [x,y], [x+2,y-1]))
                        if self.moveable(board,board[x][y],x,y,x+2,y+1,turn):
                            moves.append((board[x][y], [x,y], [x+2,y+1]))
                    if board[x][y] == -4 or board[x][y] == -5:
                        if self.moveable(board,board[x][y],x,y,x+2,y+2,turn):
                            moves.append((board[x][y], [x,y], [x+2,y+2]))
                        if self.moveable(board,board[x][y],x,y,x+2,y-2,turn):
                            moves.append((board[x][y], [x,y], [x+2,y-2]))
                        if self.moveable(board,board[x][y],x,y,x-2,y-2,turn):
                            moves.append((board[x][y], [x,y], [x-2,y-2]))
                        if self.moveable(board,board[x][y],x,y,x-2,y+2,turn):
                            moves.append((board[x][y], [x,y], [x-2,y+2]))
                    if board[x][y] == -2 or board[x][y] == -3:
                        if self.moveable(board,board[x][y],x,y,x+1,y+1,turn):
                            moves.append((board[x][y], [x,y], [x+1,y+1]))
                        if self.moveable(board,board[x][y],x,y,x+1,y-1,turn):
                            moves.append((board[x][y], [x,y], [x+1,y-1]))
                        if self.moveable(board,board[x][y],x,y,x-1,y-1,turn):
                            moves.append((board[x][y], [x,y], [x-1,y-1]))
                        if self.moveable(board,board[x][y],x,y,x-1,y+1,turn):
                            moves.append((board[x][y], [x,y], [x-1,y+1]))
                    if board[x][y] == -1:
                        if self.moveable(board,board[x][y],x,y,x+1,y,turn):
                            moves.append((-1, [x,y], [x+1,y]))
                        if self.moveable(board,board[x][y],x,y,x,y-1,turn):
                            moves.append((-1, [x,y], [x,y-1]))
                        if self.moveable(board,board[x][y],x,y,x-1,y,turn):
                            moves.append((-1, [x,y], [x-1,y]))
                        if self.moveable(board,board[x][y],x,y,x,y+1,turn):
                            moves.append((-1, [x,y], [x,y+1]))
        else:
            for x in range(10):
                for y in range(9):
                    if board[x][y] == 12 or board[x][y] == 13 or board[x][y] == 14 or board[x][y] == 15 or board[x][y] == 16:
                        if self.moveable(board, board[x][y], x, y, x-1, y, turn):
                            moves.append((board[x][y], [x,y], [x-1,y]))
                        if self.moveable(board, board[x][y], x, y, x, y-1, turn):
                            moves.append((board[x][y], [x,y], [x,y-1]))
                        if self.moveable(board, board[x][y], x, y, x, y+1, turn):
                            moves.append((board[x][y], [x,y], [x,y+1]))
                    if board[x][y] == 10 or board[x][y] == 11:
                        for i in range(10):
                            if self.moveable(board,board[x][y],x,y,i,y,turn):
                                moves.append((board[x][y], [x,y], [i,y]))
                        for i in range(9):
                            if self.moveable(board,board[x][y],x,y,x,i,turn):
                                moves.append((board[x][y], [x,y], [x,i]))
                    if board[x][y] == 8 or board[x][y] == 9:
                        for i in range(10):
                            if self.moveable(board,board[x][y],x,y,i,y,turn):
                                moves.append((board[x][y], [x,y], [i,y]))
                        for i in range(9):
                            if self.moveable(board,board[x][y],x,y,x,i,turn):
                                moves.append((board[x][y], [x,y], [x,i]))
                    if board[x][y] == 6 or board[x][y] == 7:
                        if self.moveable(board,board[x][y],x,y,x+1,y-2,turn):
                            moves.append((board[x][y], [x,y], [x+1,y-2]))
                        if self.moveable(board,board[x][y],x,y,x-1,y-2,turn):
                            moves.append((board[x][y], [x,y], [x-1,y-2]))
                        if self.moveable(board,board[x][y],x,y,x-1,y+2,turn):
                            moves.append((board[x][y], [x,y], [x-1,y+2]))
                        if self.moveable(board,board[x][y],x,y,x+1,y+2,turn):
                            moves.append((board[x][y], [x,y], [x+1,y+2]))
                        if self.moveable(board,board[x][y],x,y,x-2,y+1,turn):
                            moves.append((board[x][y], [x,y], [x-2,y+1]))
                        if self.moveable(board,board[x][y],x,y,x-2,y-1,turn):
                            moves.append((board[x][y], [x,y], [x-2,y-1]))
                        if self.moveable(board,board[x][y],x,y,x+2,y-1,turn):
                            moves.append((board[x][y], [x,y], [x+2,y-1]))
                        if self.moveable(board,board[x][y],x,y,x+2,y+1,turn):
                            moves.append((board[x][y], [x,y], [x+2,y+1]))
                    if board[x][y] == 4 or board[x][y] == 5:
                        if self.moveable(board,board[x][y],x,y,x+2,y+2,turn):
                            moves.append((board[x][y], [x,y], [x+2,y+2]))
                        if self.moveable(board,board[x][y],x,y,x+2,y-2,turn):
                            moves.append((board[x][y], [x,y], [x+2,y-2]))
                        if self.moveable(board,board[x][y],x,y,x-2,y-2,turn):
                            moves.append((board[x][y], [x,y], [x-2,y-2]))
                        if self.moveable(board,board[x][y],x,y,x-2,y+2,turn):
                            moves.append((board[x][y], [x,y], [x-2,y+2]))
                    if board[x][y] == 2 or board[x][y] == 3:
                        if self.moveable(board,board[x][y],x,y,x+1,y+1,turn):
                            moves.append((board[x][y], [x,y], [x+1,y+1]))
                        if self.moveable(board,board[x][y],x,y,x+1,y-1,turn):
                            moves.append((board[x][y], [x,y], [x+1,y-1]))
                        if self.moveable(board,board[x][y],x,y,x-1,y-1,turn):
                            moves.append((board[x][y], [x,y], [x-1,y-1]))
                        if self.moveable(board,board[x][y],x,y,x-1,y+1,turn):
                            moves.append((board[x][y], [x,y], [x-1,y+1]))
                    if board[x][y] == 1:
                        if self.moveable(board,board[x][y],x,y,x+1,y,turn):
                            moves.append((1, [x,y], [x+1,y]))
                        if self.moveable(board,board[x][y],x,y,x,y-1,turn):
                            moves.append((1, [x,y], [x,y-1]))
                        if self.moveable(board,board[x][y],x,y,x-1,y,turn):
                            moves.append((1, [x,y], [x-1,y]))
                        if self.moveable(board,board[x][y],x,y,x,y+1,turn):
                            moves.append((1, [x,y], [x,y+1]))
        
        if turn == 1:
            moves = sorted(moves, reverse=True)
            s, e = 0, 0
            for i in range(-1, -16, -1):
                tmp = []
                while e < len(moves):
                    if moves[e][0] == i:
                        tmp.append(moves[e])
                    else:
                        break
                    e = e + 1
                moves[s:e] = sorted(moves[s:e], key=lambda k: k[2])
                s = e
        else:
            moves = sorted(moves)
        return moves

    def moveable(self, board, id, x0, y0, x, y, turn):
        if x < 0 or y < 0 or x >= 10 or y >= 9:
            return False
        if turn == 1:
            if board[x][y] < 0:
                return False
            if id == -12 or id == -13 or id == -14 or id == -15 or id == -16:
                if x0 > x:
                    return False
                elif x0 <= 4 and y != y0:
                    return False
                elif abs(y - y0) + abs(x - x0) > 1:
                    return False
                else:
                    return True
            if id == -10 or id == -11:
                if board[x][y] > 0 and self.between(board, x0, y0, x, y) == 1:
                    return True
                elif board[x][y] == 0 and self.between(board, x0, y0, x, y) == 0:
                    return True
                else:
                    return False
            if id == -8 or id == -9:
                if self.between(board, x0, y0, x, y) == 0:
                    return True
                else:
                    return False
            if id == -6 or id == -7:
                if abs(y - y0) == 2:
                    if abs(x - x0) == 1 and board[x0][int((y + y0)/2)] == 0:
                        return True
                elif abs(y - y0) == 1:
                    if abs(x - x0) == 2 and board[int((x + x0)/2)][y0] == 0:
                        return True
                else:
                    return False
            if id == -4 or id == -5:
                if x > 4 :
                    return False
                if abs(y - y0) == 2 and abs(x - x0) == 2:
                    if board[int((x + x0)/2)][int((y + y0)/2)] == 0:
                        return True
                else:
                    return False
            if id == -2 or id == -3:
                if x0 == 0 or x0 == 2:
                    if x != 1:
                        return False
                if y0 == 3 or y0 == 5:
                    if y != 4:
                        return False
                if x0 == 1 and y0 == 4:
                    if x != 0 and x != 2:
                        return False
                    if y != 3 and y != 5:
                        return False
                return True
            if id == -1:
                if x > 2 or y < 3 or y > 5:
                    return False
                else:
                    return True
        else:
            if board[x][y] > 0:
                return False
            if id == 12 or id == 13 or id == 14 or id == 15 or id == 16:
                if x0 < x:
                    return False
                elif x0 >= 5 and y != y0:
                    return False
                elif abs(y - y0) + abs(x - x0) > 1:
                    return False
                else:
                    return True
            if id == 10 or id == 11:
                if board[x][y] < 0 and self.between(board, x0, y0, x, y) == 1:
                    return True
                elif board[x][y] == 0 and self.between(board, x0, y0, x, y) == 0:
                    return True
                else:
                    return False
            if id == 8 or id == 9:
                if self.between(board, x0, y0, x, y) == 0:
                    return True
                else:
                    return False
            if id == 6 or id == 7:
                if abs(y - y0) == 2:
                    if abs(x - x0) == 1 and board[x0][int((y + y0)/2)] == 0:
                        return True
                elif abs(y - y0) == 1:
                    if abs(x - x0) == 2 and board[int((x + x0)/2)][y0] == 0:
                        return True
                else:
                    return False
            if id == 4 or id == 5:
                if x < 5:
                    return False
                if abs(y - y0) == 2 and abs(x - x0) == 2:
                    if board[int((x + x0)/2)][int((y + y0)/2)] == 0:
                        return True
                else:
                    return False
            if id == 2 or id == 3:
                if x0 == 7 or x0 == 9:
                    if x != 8:
                        return False
                if y0 == 3 or y0 == 5:
                    if y != 4:
                        return False
                if x0 == 8 and y0 == 4:
                    if x != 7 and x != 9:
                        return False
                    if y != 3 and y != 5:
                        return False
                return True
            if id == 1:
                if x < 7 or y < 3 or y > 5:
                    return False
                else:
                    return True

    def between(self,board,x,y,dx,dy):
        count = 0
        if x != dx:
            if x > dx:
                x = x + dx
                dx = x - dx
                x = x - dx
            for num in range(x+1, dx):
                if board[num][y] != 0:
                    count = count + 1
            return count
        elif y != dy:
            if y > dy:
                y = y + dy
                dy = y - dy
                y = y - dy
            for num in range(y+1, dy):
                if board[x][num] != 0:
                    count = count + 1
            return count
