class ReverseInteger:

    def __init__(self):
        pass

    @staticmethod
    def reverse(x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
        sum, x = 0, abs(x)
        while x > 0:
            sum, x = sum * 10 + x % 10, x // 10
        if is_negative:
            sum = -sum
        if sum < -2147483648 or sum > 2147483647:
            sum = 0
        return sum

    def __repr__(self):
        return 'ReverseInteger'
