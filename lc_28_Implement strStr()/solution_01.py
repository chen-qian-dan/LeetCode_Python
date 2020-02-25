'''
Qian Chen
20191211Wed
'''

class Solution:
    def strStr(self, haystack: str, needle: str):
        '''
        Return the index of the first occurrence of needle in haystack.
        :param haystack: str
        :param needle: str
        :return: int
        '''
        if needle == None or len(needle) == 0:
            return 0
        elif haystack == None or len(needle) == 0:
            return -1
        elif needle in haystack:
            return haystack.index(needle)
        else:
            return -1



