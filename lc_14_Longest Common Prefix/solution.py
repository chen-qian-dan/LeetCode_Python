from _ast import List


class Solution:
    def longestCommonPrefix(self, strs):
        """
        sort, then find the common prefix of the first and last item
        :param strs:
        :return:
        """
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]

        strs.sort()
        s1 = strs[0]
        s2 = strs[-1]
        strR = ''

        for s in s1:
            if s2.startswith(strR + s):
                strR += s
            else:
                break

        return strR

