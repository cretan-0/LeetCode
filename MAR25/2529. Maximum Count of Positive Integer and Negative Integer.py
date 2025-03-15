class Solution(object):
    def maximumCount(self, nums):
        cnt_n = cnt_p = 0
        for elem in nums:
            if elem < 0:
                cnt_n += 1
            elif elem > 0:
                cnt_p += 1
        return max(cnt_n, cnt_p)
