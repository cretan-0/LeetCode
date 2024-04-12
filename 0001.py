class Solution(object):
    def twoSum(self, nums, target):
        if nums == {0}:
            return 0
	    
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return i, j
        return 0    
