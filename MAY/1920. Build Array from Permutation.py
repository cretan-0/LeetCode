class Solution(object):
    def buildArray(self, nums):
        res = []
        for i in range(len(nums)):
            a = nums[nums[i]]
            res.append(a)
        return res
        
