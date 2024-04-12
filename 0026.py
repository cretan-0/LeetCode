class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        nums.sort() # be sure the list is sorted 
        k = 1;
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i];
                k += 1
        return k