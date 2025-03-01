class Solution(object):
    def move_zeros(self, nums):
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]  
                if non_zero_index != i:  
                    nums[i] = 0
                non_zero_index += 1
        return nums

    def applyOperations(self, nums):
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
                i+=1
            i+=1

        return self.move_zeros(nums)


def main() -> None:
    sol = Solution()
    nums = [1,2,2,1,1,0]
    print(sol.applyOperations(nums))

if __name__ == '__main__':
    main()
