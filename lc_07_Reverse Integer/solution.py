class Solution:
    def reverse(self, x: int) -> int:

        strSign = ''
        if x < 0:
            x *= -1
            strSign = '-'
        print(str(x))

        strReversed = strSign + ''.join(reversed(str(x)))
        if int(strReversed) in range(-2**31, 2**31):
            return int(strReversed)

        return 0


