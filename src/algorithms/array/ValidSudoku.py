from typing import List


class ValidSudoku:

    def __init__(self):
        pass

    @staticmethod
    def is_valid_sudoku(board: List[List[str]]) -> bool:
        for row in range(0, len(board)):
            for col in range(0, len(board[row])):
                if board[row][col] != "." and not ValidSudoku.check_valid(board, row, col):
                    return False
        return True

    @staticmethod
    def check_valid(board: List[List[str]], row: int, col: int) -> bool:
        # row check
        for index in range(0, len(board)):
            if index != col and board[row][index] == board[row][col]:
                return False

        # column check
        for index in range(0, len(board)):
            if index != row and board[index][col] == board[row][col]:
                return False

        # box check
        for index in range(0, len(board)):
            row_x = 3 * (row // 3) + (index // 3)
            col_y = 3 * (col // 3) + (index % 3)
            if row != row_x and col != col_y and board[row_x][col_y] == board[row][col]:
                return False
        return True

    def __repr__(self):
        return 'ValidSudoku'
