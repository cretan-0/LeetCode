# https://leetcode.com/problems/divide-array-into-equal-pairs/description/
# https://leetcode.com/problems/modify-the-matrix/

from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k:
            minim = min(nums)
            for i in range(len(nums)):
                count_min = 0
                first_occurance = 0
                if nums == minim:
                    first_occurance = i
                    count_min += 1
                    print(count_min)
                if count_min > 1:
                    nums[first_occurance] = nums[first_occurance] * multiplier
                if count_min == 1:
                    nums[first_occurance] = nums[first_occurance] * multiplier
                break
            k -= 1
        return nums


def main() -> None:
    sol = Solution()
    nums = [2, 1, 3, 5, 6]
    k = 5
    multiplier = 2
    print(sol.getFinalState(nums, k, multiplier))

    print(3%3)

if __name__ == "__main__":
    main()
