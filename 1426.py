class Solution:
    def countNumber(self, nums):
        counter = 0
        for num in nums:
            x = num + 1
            if x in nums:
                counter += 1
        return counter

def main() -> None:
    sol = Solution()
    nums = [1,1,3,3,5,5,7,7]
    print(sol.countNumber(nums))

if __name__ == "__main__":
    main()
