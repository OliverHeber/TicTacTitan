from ai import AI
from board import Board
from constants import *

class TicTacToe:
    def __init__(self) -> None:
        self.board = Board()
        self.player = 1
        self.playing = True
        # self.gamemode = 'pvp'
        self.gamemode = 'ai'
        self.ai = AI()

    def draw_board(self, p, screen):
        # Horizontal lines
        p.draw.line(screen, LINE_COLOR, (0, SQ_SIZE), (WIDTH, SQ_SIZE), LINE_WIDTH)
        p.draw.line(screen, LINE_COLOR, (0, HEIGHT - SQ_SIZE), (WIDTH, HEIGHT - SQ_SIZE), LINE_WIDTH)

        # Vertical lines
        p.draw.line(screen, LINE_COLOR, (SQ_SIZE, 0), (SQ_SIZE, HEIGHT), LINE_WIDTH)
        p.draw.line(screen, LINE_COLOR, (WIDTH - SQ_SIZE, 0), (WIDTH - SQ_SIZE, HEIGHT), LINE_WIDTH)
    
    def change_player_parity(self):
        self.player = self.player % 2 + 1
    
    def draw_move(self, p, screen, row, col):
        if self.player == 1:
            # Draw descending portion of cross
            start_d = (col * SQ_SIZE + OFFSET, row * SQ_SIZE + OFFSET)
            end_d = (col * SQ_SIZE + SQ_SIZE - OFFSET, row * SQ_SIZE + SQ_SIZE - OFFSET)
            p.draw.line(screen, CROSS_COLOUR, start_d, end_d, CROSS_WIDTH)

            # Draw ascending portion of cross
            start_a = (col * SQ_SIZE + OFFSET, row * SQ_SIZE + SQ_SIZE - OFFSET)
            end_a = (col * SQ_SIZE + SQ_SIZE - OFFSET, row * SQ_SIZE + OFFSET)
            p.draw.line(screen, CROSS_COLOUR, start_a, end_a, CROSS_WIDTH)

        else:
            p.draw.circle(screen,
                          CIRCLE_COLOUR,
                          (col * SQ_SIZE + SQ_SIZE // 2, row * SQ_SIZE + SQ_SIZE // 2),
                          CIRCLE_RADIUS,
                          CIRCLE_WIDTH)