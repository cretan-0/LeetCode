class Solution(object):
    def waysToSplitArray(self, nums):
        counter = 0
        left_sum = 0
        total_sum = sum(nums)

        for i in range(len(nums)-1):
            left_sum += nums[i]
            right_sum = total_sum - left_sum 
            if left_sum >= right_sum:
                counter +=1
        return counter

def main() -> None:
    sol = Solution()
    nums = [9,9,9]
    print(sol.waysToSplitArray(nums))


if __name__ == "__main__":
    main()
