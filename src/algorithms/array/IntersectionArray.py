from typing import List


class IntersectionArray:

    def __init__(self):
        pass

    @staticmethod
    def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return IntersectionArray.intersect(nums2, nums1)
        smaller, nums1, nums2, result = len(nums1), sorted(nums1), sorted(nums2), []
        for index in range(0, smaller):
            if nums1[index] in nums2:
                result.append(nums1[index])
                nums2.remove(nums1[index])
        return sorted(result)

    def __repr__(self):
        return 'IntersectionArray'
