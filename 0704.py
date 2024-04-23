class Solution(object):
    def search(self, nums, target):
        start = 0
        mid = 0
        end = len(nums) - 1
        while (start <= end):
            mid = (start+end)//2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1