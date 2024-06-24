class Solution(object):
    def minimumAverage(self, nums):
        if len(nums) % 2 != 0:
            return
        averages = []
        nums.sort()
        for i in range(len(nums)):
            if nums:
                averages.append(float(nums[0] + nums[-1])/2)
                nums.remove(nums[0])
                nums.remove(nums[-1])
            else:
                break
        return min(averages)

def main() -> None:
    sol = Solution()
    nums = [7,8,3,4,15,13,4,1]
    print(sol.minimumAverage(nums))

if __name__ == "__main__":
    main()
