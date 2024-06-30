class Solution(object):
    def maximumLength(self, nums):
        counter = 1
        sub_array = []
        last_elem = 0
        same_parity = True
        for i in range(len(nums)-1):
            if nums[i] % 2 == 0 and nums[i+1] % 2 == 1:
                same_parity = False
        for i in range(len(nums)-1):
            if nums[i] % 2 == 1 and nums[i+1] % 2 == 0:
                same_parity = False
        for i in range(len(nums)-1):
            if (nums[i] % 2 == 0 and nums[i+1] % 2 == 1) or (nums[i] % 2 == 1 and nums[i+1] % 2 == 0):
                sub_array.append(nums[i])
                last_elem = nums[i+1]
        #print(last_elem)
        sub_array.append(last_elem)
        return len(nums) if same_parity else len(sub_array)

"""

class Solution(object):
    def maximumLength(self, nums):
        counter = 0
        sub_array = []
        last_elem = 0
        same_parity = True
        for i in range(len(nums)-1):
            if nums[i] % 2 == 0 and nums[i+1] % 2 == 1 or nums[i] % 2 == 1 and nums[i+1] % 2 == 0:
                same_parity = False






        for i in range(len(nums)-2):
            if (nums[i] + nums[i+1]) % 2 == (nums[i+1] + nums[i+2]) % 2:
                print(nums[i], " ", nums[i+1], " ", nums[i+2])
                sub_array.append(nums[i])


                last_elem = nums[-1]
        print(last_elem)
        sub_array.append(last_elem)

        print(sub_array)
        #return len(nums) if same_parity else len(sub_array)




def main() -> None:
    sol = Solution()
    nums = [1,1,7,3,2]
    print(sol.maximumLength(nums)) # out: 3 -> exp: 4
    '''
    1+1 = 2
    1+7 = 8
    
    1+7 = 8 
    7+3 = 10
    
    7+3 = 10
    3+2 = 5
    '''


if __name__ == "__main__":
    main()




"""
