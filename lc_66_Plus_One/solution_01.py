"""
Qian Chen
20191218Wed
"""


class Solution:
    def plusOne(self, digits):
        '''
        :param digits: List[int]
        :return: List[int]
        '''
        string = ""
        for s in digits:
            string += str(s)

        n = int(string)
        n += 1
        strs = str(n)
        ret = []
        ret.extend(strs)

        return ret