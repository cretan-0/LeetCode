class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        counter = 0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)):
                if nums[j] - nums[i] != diff:
                    continue
                for k in range(j+1, len(nums)):
                    if nums[k] - nums[j] == diff:
                        counter += 1
        return counter





def main() -> None:
    sol = Solution()
    nums = [0,1,4,6,7,10]
    diff = 3
    print(sol.arithmeticTriplets(nums, diff))

if __name__ == "__main__":
    main()

    # make 4Sum