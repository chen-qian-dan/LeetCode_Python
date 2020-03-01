from _ast import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()

        if len(nums1) % 2 == 1:
            index = len(nums1) // 2
            return nums1[index]

        index = len(nums1) // 2
        return (nums1[index] + nums1[index - 1]) * 0.5


