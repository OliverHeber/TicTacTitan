import sys
import pygame as p
from constants import *
from tictactoe import TicTacToe

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    p.display.set_caption("Tic Tac Toe")
    screen.fill(SCREEN_COLOR)

    ttt = TicTacToe()
    ttt.draw_board(p, screen)

    ai = ttt.ai

    while True:
        for e in p.event.get():
            if e.type == p.QUIT:
                p.quit()
                sys.exit()
            if e.type == p.MOUSEBUTTONDOWN:
                col, row = e.pos
                col, row = col // SQ_SIZE, row // SQ_SIZE
                
                if ttt.board.check_empty_square(row, col):
                    ttt.board.make_move(ttt.player, row, col)
                    ttt.draw_move(p, screen, row, col)
                    ttt.change_player_parity()
                    ttt.board.check_win(p, screen)
                
        if ttt.gamemode == "ai" and ttt.player == ai.player:
            p.display.update()
            row, col = ai.eval(p, screen, ttt.board)
            ttt.board.make_move(ai.player, row, col)
            ttt.draw_move(p, screen, row, col)
            ttt.change_player_parity()

        p.display.update()

if __name__ == "__main__":
    main()