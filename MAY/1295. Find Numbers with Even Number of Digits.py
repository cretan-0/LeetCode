class Solution(object):
    def findNumbers(self, nums):
        out = 0
        for elem in nums:
            cnt = 0
            while elem:
                elem = elem // 10
                cnt += 1
            if cnt % 2 == 0:
                out += 1
        return out
