from typing import List


class SingleNumber:

    def __init__(self):
        pass

    @staticmethod
    def single_number(nums: List[int]) -> int:
        single = 0
        for num in nums:
            single = num ^ single
        return single

    def __repr__(self):
        return 'SingleNumber'
