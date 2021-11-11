from typing import List


class RotateArray:

    def __init__(self):
        pass

    @staticmethod
    def rotate(nums: List[int], k: int) -> None:
        k = k % len(nums) if k > len(nums) else k
        n = len(nums)
        result = [0] * n
        for i in range(n):
            result[(i + k) % n] = nums[i]
        nums[:] = result

    def __repr__(self):
        return 'RotateArray'
