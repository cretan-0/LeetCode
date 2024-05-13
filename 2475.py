class Solution(object):
    def unequalTriplets(self, nums):
        counter = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    continue
                for k in range(j+1, len(nums)):
                    if nums[i] != nums[k] and nums[j] != nums[k]:
                        counter+=1
        return counter



def main() -> None:
    sol = Solution()
    nums = [1,1,1,1,1]
    print(sol.unequalTriplets(nums))

if __name__ == "__main__":
    main()