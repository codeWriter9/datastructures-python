from typing import List


class BinarySearch:

    def __init__(self):
        pass

    @staticmethod
    def search(nums: List[int], target: int) -> int:
        index = -1
        left = 0
        right = len(nums)
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] < target:
                left = left + 1
            elif nums[mid] > target:
                right = right - 1
            else:
                return mid
        return index

    def __repr__(self):
        return 'BinarySearch'
