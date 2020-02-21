class Solution:
    def isPalindrome(self, x: int) -> bool:
        strForward = str(x)
        strBackward = ''.join(reversed(strForward))
        if strForward == strBackward:
            return True
        return False