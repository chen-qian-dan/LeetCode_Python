class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sts = s.strip().split(' ')
        return len(sts[-1])

