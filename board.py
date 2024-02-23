import numpy as np
from constants import *

class Board:
    def __init__(self) -> None:
        self.squares = np.zeros((ROWS, COLS))
        self.marked_squares = 0
        self.empty_sqaures = self.squares
    
    def make_move(self, player, row, col):
        self.marked_squares += 1
        self.squares[row][col] = player
    
    def check_empty_square(self, row, col):
        return self.squares[row][col] == 0

    def is_full(self):
        return self.marked_squares == 9

    def is_empty(self):
        return self.marked_squares == 0

    def get_empty_squares(self):
        empty_squares = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.check_empty_square(row, col):
                    empty_squares.append((row, col))
        return empty_squares

    def check_win(self, p, screen):
        # vertical wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                color = CIRCLE_COLOUR if self.squares[0][col] == 2 else CROSS_COLOUR
                p.draw.line(screen,
                             color, 
                             (col * SQ_SIZE + SQ_SIZE // 2, 20), 
                             (col * SQ_SIZE + SQ_SIZE // 2, HEIGHT - 20), 
                             LINE_WIDTH)
                return self.squares[0][col]

        # horizontal wins
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                color = CIRCLE_COLOUR if self.squares[row][0] == 2 else CROSS_COLOUR
                p.draw.line(screen,
                             color,
                             (20, row * SQ_SIZE + SQ_SIZE // 2),
                             (WIDTH - 20, row * SQ_SIZE + SQ_SIZE // 2),
                             LINE_WIDTH)
                return self.squares[row][0]

        # desc diagonal
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            color = CIRCLE_COLOUR if self.squares[1][1] == 2 else CROSS_COLOUR
            iPos = (20, 20)
            fPos = (WIDTH - 20, HEIGHT - 20)
            p.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)
            return self.squares[1][1]

        # asc diagonal
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            color = CIRCLE_COLOUR if self.squares[1][1] == 2 else CROSS_COLOUR
            iPos = (20, HEIGHT - 20)
            fPos = (WIDTH - 20, 20)
            p.draw.line(screen, color, iPos, fPos, CROSS_WIDTH)
            return self.squares[1][1]

        # no win yet
        return 0