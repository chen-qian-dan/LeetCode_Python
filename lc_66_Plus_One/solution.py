class Solution:
    def plusOne(self, digits):
        # list to string -> number -> + 1 -> number to list
        strNum = ''.join(map(str, digits))
        num = int(strNum) + 1

        # list comprehension
        ret = [int(ele) for ele in str(num)]

        return ret


