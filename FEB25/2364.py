# TLE - O(n*2)
class Solution(object):
    def countBadPairs(self, nums):
        cnt = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if j - nums[j] != i - nums[i]:
                    cnt += 1
        return cnt
        
