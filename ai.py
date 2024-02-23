import copy
import random


class AI:
    def __init__(self, type = 1, player = 2) -> None:
        self.type = type
        self.player = player
    
    def minimax(self, p, screen, board, is_maximising):
        # terminal case
        state = board.check_win(p, screen)

        # player 1 wins
        if state == 1:
            return 1, None # eval, move

        # player 2 wins
        if state == 2:
            return -1, None

        # draw
        elif board.is_full():
            return 0, None

        if is_maximising:
            max_eval, best_move, empty_sqrs = -100, None ,board.get_empty_squares()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.make_move(1, row, col)
                eval = self.minimax(p, screen, temp_board, False)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)

            return max_eval, best_move

        elif not is_maximising:
            min_eval, best_move, empty_sqrs = 100, None ,board.get_empty_squares()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.make_move(self.player, row, col)
                eval = self.minimax(p, screen, temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)

            return min_eval, best_move
    
    def eval(self, p, screen, board):
        # Generate a random choice
        if self.type == 0:
            empty_squares = board.get_empty_squares()
            move = empty_squares[random.randrange(0, len(empty_squares))]
        else:
            _, move = self.minimax(p, screen, board, False)

        return move # (row, col)