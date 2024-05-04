class Solution(object):
    def maximumCount(self, nums):
        nums.sort()
        counter_min = 0
        counter_max = 0
        for num in nums:
            if num < 0:
                counter_min += 1
            if num > 0:
                counter_max += 1
        return max(counter_min, counter_max)