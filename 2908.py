class Solution(object):
    def minimumSum(self, nums):
        list_sums = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                if nums[i] >= nums[j]:
                    continue
                for k in range(j+1, len(nums)):
                    if nums[k] < nums[j]:
                        sum = nums[i] + nums[j] + nums[k]
                        list_sums.append(sum)
        if list_sums:
            return min(list_sums)
        else:
            return -1


def main() -> None:
    sol = Solution()
    nums = [5,4,8,7,10,2]
    print(sol.minimumSum(nums))

if __name__ == "__main__":
    main()
