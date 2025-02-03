class Solution(object):
    def srt(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        return nums


    def rotate(self, nums, k):
        k = k % len(nums)
        self.srt(nums, 0, len(nums) - 1)
        self.srt(nums, 0, k-1)
        self.srt(nums, k, len(nums) - 1)
        return nums
