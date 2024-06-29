# buble sort
class Solution(object):
    def sortColors(self, nums):
        made_a_swap = True
        n = len(nums)
        while made_a_swap:
            made_a_swap = False
            for i in range(n-1):
                if nums[i] > nums[i+1]:
                    temp = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = temp
                    made_a_swap = True
        return nums

def main() -> None:
    sol = Solution()
    nums = [2,0,2,1,1,0]
    print(sol.sortColors(nums))

if __name__ == "__main__":
    main()


