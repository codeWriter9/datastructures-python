from typing import List


class MoveZeroes:

    def __init__(self):
        pass

    @staticmethod
    def move_zeroes(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count = zero_count + 1
        if len(nums) > zero_count:
            slow = 0
            for fast in range(0, len(nums)):
                if nums[fast] != 0:
                    nums[slow] = nums[fast]
                    slow = slow + 1
            while slow < len(nums):
                nums[slow] = 0
                slow = slow + 1

    def __repr__(self):
        return 'MoveZeroes'
