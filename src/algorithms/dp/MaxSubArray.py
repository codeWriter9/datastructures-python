from typing import List


class MaxSubArray:

    def __init__(self):
        pass

    @staticmethod
    def max_sub_array(nums: List[int]) -> int:
        if nums:
            global_max_sum = nums[0]
            local_max_sum = nums[0]
            for num in nums[1:]:
                local_max_sum = max(num, num + local_max_sum) # Does addition reduce the sum
                global_max_sum = max(global_max_sum, local_max_sum)
            return global_max_sum
        return 0

    def __repr__(self):
        return 'MaxSubArray'
