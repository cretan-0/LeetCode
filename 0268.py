https://leetcode.com/problems/missing-number/solutions/5580856/simple-solution-in-python-beats-90-98/

class Solution(object):
    def missingNumber(self, nums):
        # let's see the length of nums (useful in for loop)
        length = len(nums) + 1
        # list with all numbers that should be in that range, here will be present the missing number
        list_of_nums = []
        # let's loop over each element in that range
        for num in range(length):
            # here we'll have all numbers that should be present 
            list_of_nums.append(num)
        # in res variable will have difference between those 2 lists (initial one: nums, the new one: list_of_nums)
        res = list((set(list_of_nums) - set(nums)))
        # res is now a list that contain the only number which is missing
        # in this manner we'll convert the list to an integer number.
        number = int(''.join(str(digit) for digit in res))
        # return the number which is missing
        return number


def main() -> None:
    sol = Solution()
    nums = [9,6,4,2,3,5,7,0,1]
    print(sol.missingNumber(nums))

if __name__ == "__main__":
    main()
