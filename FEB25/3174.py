class Solution(object):
    def clearDigits(self, s):
        res = []
        for char in s:
            if char.isdigit():
                if res:
                    res.pop()
            else:
                res.append(char)
        return ''.join(res)
