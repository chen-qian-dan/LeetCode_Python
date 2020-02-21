class Solution:
    def romanToInt(self, s: str) -> int:
        rom2int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        nRet = 0
        for i in range(0, len(s)):
            if i < len(s)-1 and rom2int[s[i]] < rom2int[s[i+1]]:
                nRet -= rom2int[s[i]]
            else:
                nRet += rom2int[s[i]]

        return nRet


a = Solution()
print(a.romanToInt("MCMXCIV"))