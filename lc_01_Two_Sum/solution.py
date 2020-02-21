from _ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(0, len(nums)-1):
            nGap = target - nums[i]
            for j in range(i+1, len(nums)):
                if nGap == nums[j]:
                    return [i, j]

