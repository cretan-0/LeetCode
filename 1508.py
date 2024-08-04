# Runtime 293ms, Beats 71.43%
# Memory 47.12MB, 14.29%

class Solution(object):
    def rangeSum(self, nums, n, left, right):
        new_arr = []
        for i in range(n):
            sum = nums[i]
            new_arr.append(nums[i])
            for j in range(i+1, n):
                sum += nums[j]
                new_arr.append(sum)
        res = 0
        new_arr = sorted(new_arr)
        for i in range(left-1, right):
            res += new_arr[i]
        return res % (pow(10, 9) + 7)

def main() -> None:
    sol = Solution()
    nums = [1,2,3,4]
    n = 4
    left = 1
    right = 5
    print(sol.rangeSum(nums, n, left, right))

if __name__ == "__main__":
    main()

