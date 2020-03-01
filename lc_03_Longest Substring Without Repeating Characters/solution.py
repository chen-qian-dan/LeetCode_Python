class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strRet = ''
        strCur = ''

        nCur = 0
        i = nCur
        while i < len(s):
            if s[i] not in strCur:
                strCur += s[i]
                i += 1
            else:
                if len(strCur) > len(strRet):
                    strRet = strCur
                nCur += 1
                i = nCur
                strCur = ''

        if len(strCur) > len(strRet):
            strRet = strCur

        return len(strRet)


a = Solution()
print(a.lengthOfLongestSubstring('aab'))