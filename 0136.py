class Solution(object):
    def singleNumber(self, nums):
        ans  = 0
        for num in nums:
            ans ^= num
        return ans


"""
2nd solution
class Solution(object):
    def singleNumber(self, nums):
        for num in nums:
            if nums.count(num) == 1:
                return num
"""