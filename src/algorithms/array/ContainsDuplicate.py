from typing import List


class ContainsDuplicate:

    def __init__(self):
        pass

    @staticmethod
    def containsDuplicate(nums: List[int]) -> bool:
        return not len(nums) == len(set(nums))

    def __repr__(self):
        return 'ContainsDuplicate'
