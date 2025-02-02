class Solution(object):
    def isArraySpecial(self, nums):
        if len(nums) == 1:
            return True
        for i in range(len(nums)-1):
            if (nums[i] % 2 == 1 and nums[i+1] % 2 == 1) or (nums[i] % 2 == 0 and nums[i+1] % 2 == 0):
                return False
        return True


# v2

'''
Generally, odd + odd -> even 
           even + even -> even
           even + odd -> odd
'''

class Solution(object):
    def isArraySpecial(self, nums):
        for i in range(len(nums)-1):
            if (nums[i]+nums[i+1]) % 2 == 0:
                return False
        return True

#v3

class Solution(object):
    def isArraySpecial(self, nums):
        return all((nums[i] & 1 != nums[i+1] & 1) for i in range(len(nums)-1))
