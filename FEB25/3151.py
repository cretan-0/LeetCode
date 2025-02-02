class Solution(object):
    def isArraySpecial(self, nums):
        if len(nums) == 1:
            return True
        for i in range(len(nums)-1):
            if (nums[i] % 2 == 1 and nums[i+1] % 2 == 1) or (nums[i] % 2 == 0 and nums[i+1] % 2 == 0):
                return False
        return True
