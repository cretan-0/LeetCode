class Solution(object):
    def maximumSum(self, nums):
        maxim = -1
        sum_digits = {}
        for num in nums:
            index = sum(int(digits) for digits in str(num))
            if index in sum_digits:
                maxim = max(maxim, num+sum_digits[index])
                sum_digits[index] = max(sum_digits[index], num)
            else:
                sum_digits[index] = num

        return maxim if maxim != -1 else 0


def main() -> None:
    sol = Solution()
    nums = [18,43,36,13,7]
    print(sol.maximumSum(nums))

if __name__ == "__main__":
    main()
