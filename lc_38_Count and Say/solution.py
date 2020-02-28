class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        strOld = '1'
        strNew = ''
        for i in range(1, n):
            curVal = strOld[0]
            count = 0
            for index, val in enumerate(strOld, 0):
                if val == curVal:
                    count += 1
                else:
                    strNew += str(count) + curVal
                    curVal = val
                    count = 1
            strNew += str(count) + curVal
            strOld = strNew
            strNew = ''
        return strOld




a = Solution()
print(a.countAndSay(1))
print(a.countAndSay(2))
print(a.countAndSay(3))
print(a.countAndSay(4))
print(a.countAndSay(5))
print(a.countAndSay(6))




