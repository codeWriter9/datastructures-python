from typing import List


class MaxSubArray:

    def __init__(self):
        pass

    @staticmethod
    def max_sub_array(nums: List[int]) -> int:
        if nums:  # check if the nums is not null or empty
            global_max_sum = nums[0]  # set first element as global maxima
            local_max_sum = nums[0]  # set first element as local maxima
            for num in nums[1:]:  # for all elements in array
                local_max_sum = max(num, num + local_max_sum) # check if adding the current element lessens the sum
                global_max_sum = max(global_max_sum, local_max_sum) # check if current sum is less than the global sum
            return global_max_sum
        return 0

    def __repr__(self):
        return 'MaxSubArray'
