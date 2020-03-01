class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = len(s)

        while max_len > 1:
            for i in range(0, len(s)-max_len + 1):
                substring = s[i: i + max_len]
                if substring == substring[::-1]:
                    return substring
            max_len -= 1
        return (s[0] if s else '')


