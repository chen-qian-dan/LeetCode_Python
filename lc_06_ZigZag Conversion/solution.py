class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        n_len = 2 * numRows - 2  # minus the head and tail

        str_ret = ''
        arr = list()
        i = 0
        while i < len(s):
            arr.append(s[i:i+n_len])
            i += n_len

        for i, st in enumerate(arr):
            str_ret += st[0]
            arr[i] = st[1:]

        count = n_len - 1
        while len(arr[0]) > 0:
            for i, value in enumerate(arr):
                if count == len(value) >= 2:
                    str_ret += value[0]
                    str_ret += value[-1]
                    arr[i] = value[1:-1]

                elif len(value) == 1:
                    str_ret += value[0]
                    arr[i] = ''

                elif count > len(value) >= 2:
                    str_ret += value[0]
                    arr[i] = value[1:]

            count -= 2
        return str_ret

a = Solution()
print(a.convert('P', 1))