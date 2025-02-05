class Solution(object):
    def maxAscendingSum(self, nums):
        res = 0
        temp_val = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                temp_val += nums[i]
            else:
                res = max(res, temp_val)
                temp_val = nums[i]
        res = max(res, temp_val)
        return res
