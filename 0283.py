# https://leetcode.com/problems/move-zeroes/solutions/5582546/python-solution-runtime-108ms-beats-90-92/

class Solution(object):
    def moveZeroes(self, nums):
        k = 0
        for idx, num in enumerate(nums):
            if num != 0:
                nums[idx], nums[k] = nums[k], nums[idx]
                k+=1
        return nums

def main() -> None:
    sol = Solution()
    nums = [0,1,0,3,12]
    print(sol.moveZeroes(nums))

if __name__ == "__main__":
    main()
