class Solution(object):
    def maximumTripletValue(self, nums):
        list_nums = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    val = (nums[i] - nums[j]) * nums[k]
                    list_nums.append(val)
        if len(list_nums) == 3 or max(list_nums) < 0:
            return 0
        else:
            return max(list_nums)



def main() -> None:
    sol = Solution()
    nums = [1,2,3]
    print(sol.maximumTripletValue(nums))

if __name__ == "__main__":
    main()