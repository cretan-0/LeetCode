class Solution(object):
    def twoSum(self, nums, target):
        if nums == {0}:
            return 0
	    
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return i, j
        return 0    


# V2:
class Solution(object):
    def twoSum(self, nums, target):
        res = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
        return res
