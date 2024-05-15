class Solution(object):
    def numIdenticalPairs(self, nums):
        counter = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i < j and nums[i] == nums[j]:
                   counter += 1
        return counter



def main() -> None:
    sol = Solution()
    nums = [1,1,1,1]
    print(sol.numIdenticalPairs(nums))


if __name__ == "__main__":
    main()