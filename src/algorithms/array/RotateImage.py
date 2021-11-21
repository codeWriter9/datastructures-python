from typing import List


class RotateImage:

    def __init__(self):
        pass

    @staticmethod
    def transpose(matrix: List[List[int]]) -> None:
        for row in range(0, len(matrix)):
            for col in range(row, len(matrix[row])):
                matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]

    @staticmethod
    def reflect(matrix: List[List[int]]) -> None:
        for row in range(0, len(matrix)):
            for col in range(0, int(len(matrix[row]) / 2)):
                matrix[row][col], matrix[row][len(matrix) - col - 1] = matrix[row][len(matrix) - col - 1], matrix[row][col]

    @staticmethod
    def rotate(matrix: List[List[int]]) -> None:
        RotateImage.transpose(matrix)
        RotateImage.reflect(matrix)

    def __repr__(self):
        return 'RotateImage'
