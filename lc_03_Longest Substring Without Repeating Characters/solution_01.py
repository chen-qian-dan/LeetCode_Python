class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strCur = list()
        max_length = 0

        for i, value in enumerate(s):

            if value in strCur:
                max_length = max(max_length, len(strCur))
                index = strCur.index(value)
                strCur = strCur[index + 1:]

            strCur.append(value)

        max_length = max(max_length, len(strCur))

        return max_length