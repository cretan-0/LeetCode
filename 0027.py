class Solution(object):
    def removeElement(self, nums, val):
        if len(nums) == 0:
            return 0
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k