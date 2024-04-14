class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            else:
                y = nums.append(target)
                nums.sort()
                for j in range(len(nums)):
                    if nums[j] == target:
                        return j
            