from _ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # only work when there is no duplication item in nums.
        checked = {}
        for i, v in enumerate(nums, 0):
            remaining = target - v
            if remaining in checked:
                return [checked[remaining], i]
            else:
                checked[v] = i
        return []
