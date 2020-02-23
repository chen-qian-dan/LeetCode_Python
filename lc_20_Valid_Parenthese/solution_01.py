
"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

Qian Chen
20191207Sat
"""


class Solution:
    def isValid(self, s):
        '''
        :param s: str
        :return: bool
        '''
        dic = {"(": ")",
               "{": "}",
               "[": "]"}

        left = ["(", "{", "["]
        right = [")", "}", "]"]

        s_left = ""

        if len(s) % 2 != 0:
            return False
        elif not s:
            return True
        elif s[0] in right:
            return False

        for char in s:
            if char in left:
                s_left += char
            elif char in right:
                last_l = s_left[-1]
                if dic.get(last_l) == char:
                    s_left = s_left[:-1]
                else:
                    return False

        if s_left:
            return False
        else:
            return True









