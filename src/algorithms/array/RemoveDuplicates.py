from typing import List


class RemoveDuplicates:

    def __init__(self):
        pass

    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow = slow + 1
                nums[slow] = nums[fast]
        return slow + 1

    def __repr__(self):
        return 'RemoveDuplicates'
