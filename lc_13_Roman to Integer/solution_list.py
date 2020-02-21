"""
The method is check from left to right,
check 2 letters first, then check 1 letter.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        ret = 0
        rom2int = {"I": 1,
                   "V": 5,
                   "X": 10,
                   "L": 50,
                   "C": 100,
                   "D": 500,
                   "M": 1000,
                   "IV": 4,
                   "IX": 9,
                   "XL": 40,
                   "XC": 90,
                   "CD": 400,
                   "CM": 900}

        while len(s) > 0:
            if len(s) == 1:
                if s in rom2int:
                    ret += rom2int.get(s)
                    s = ""
            else:
                sub = s[:2]
                is_combined = False
                if sub in rom2int:
                    ret += rom2int.get(sub)
                    s = s[2:]
                    is_combined = True

                if not is_combined:
                    sub = s[0]
                    if sub in rom2int:
                        ret += rom2int.get(sub)
                        s = s[1:]
        return ret
