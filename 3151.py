class Solution(object):
    def isArraySpecial(self, nums):
        if len(nums) == 1:
            return True
        dif_adjacent_parity = True
        for i in range(len(nums)-1):
            print(nums[i], " ", nums[i+1])
            if (nums[i] % 2 == 0 and nums[i+1] % 2 == 0) or (nums[i] % 2 == 1 and nums[i+1] % 2 == 1):
                dif_adjacent_parity = False
        return dif_adjacent_parity





def main() -> None:
    sol = Solution()
    nums = [1,2]
    print(sol.isArraySpecial(nums))


if __name__ == "__main__":
    main()
