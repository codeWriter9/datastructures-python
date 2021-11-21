from typing import List


class ReverseString:

    def __init__(self):
        pass

    @staticmethod
    def reverse_string(s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for index in range(0, int(len(s) / 2)):
            s[index], s[len(s) - 1 - index] = s[len(s) - 1 - index], s[index]

    def __repr__(self):
        return 'ReverseString'
