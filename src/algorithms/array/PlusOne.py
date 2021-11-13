from typing import List


class PlusOne:

    def __init__(self):
        pass

    @staticmethod
    def plus_one(digits: List[int]) -> List[int]:
        if len(digits) == 1 and digits[0] == 0:
            return [1]
        carry_over = 1  # Add one
        for reverse_index in range(len(digits) - 1, -1, -1):
            digits[reverse_index], carry_over = (digits[reverse_index] + carry_over) % 10, int((digits[reverse_index] + carry_over) / 10)
        if carry_over > 0:
            new_digits = [0] * (len(digits) + 1)
            for index in range(1, len(digits)):
                new_digits[index] = digits[index]
            new_digits[0], digits = carry_over, new_digits

        return digits

    def __repr__(self):
        return 'PlusOne'
