from typing import List


class TwoSum:

    def __init__(self):
        pass

    @staticmethod
    def two_sum(nums: List[int], target : int) -> List[int]:
        _dict_ = dict()
        for index in range(0, len(nums)):
            complement = target - nums[index]
            if complement in _dict_:
                return sorted([index, _dict_[complement]])
            else:
                _dict_[nums[index]] = index
        pass

    def __repr__(self):
        return 'TwoSum'
