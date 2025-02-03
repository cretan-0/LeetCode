class Solution(object):
    def check(self, nums):
        if not nums:
            return True

        count_break = 0
        for i in range(len(nums)):
            if nums[i] > nums[(i + 1) % len(nums)]:
                count_break += 1

        return count_break < 2
        
