# Runtime: 2361ms, Beats 9.69%
# Memory: 13.09MB, Beats 78.06%

class Solution(object):
    def singleNumber(self, nums):
        new_arr = []
        for num in nums:
            if nums.count(num) < 2:
                new_arr.append(num)
        return new_arr


def main() -> None:
    sol = Solution()
    nums = [-1,0]
    print(sol.singleNumber(nums))

if __name__ == "__main__":
    main()

