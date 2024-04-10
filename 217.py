class Solution(object):
    def containsDuplicate(self, nums):
        for i in nums:
            if nums.count(i) > 1:
                return True