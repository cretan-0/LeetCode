class Solution(object):
    def maximumDifference(self, nums):
        maxim = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                r = nums[j] - nums[i]
                maxim = max(r, maxim)
        if maxim:
            return maxim
        else:
            return -1
        
