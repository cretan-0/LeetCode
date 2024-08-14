class Solution(object):
    def thirdMax(self, nums):
        nums = set(nums)
        nums = list(nums)
        if len(nums) < 3:
            return max(nums)
        else:
            nums = sorted(nums, reverse=True)
            return nums[2]

def main() -> None:
    sol = Solution()
    nums = [2,2,3,1]
    print(sol.thirdMax(nums))

if __name__ == "__main__":
    main()

