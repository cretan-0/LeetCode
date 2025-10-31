from collections import Counter
class Solution(object):
    def getSneakyNumbers(self, nums):
        cnt = Counter(nums)
        return [num for num, freq in cnt.items() if freq == 2]        

        
def main():
    solution = Solution()
    nums = [7,1,5,4,3,4,6,0,9,5,8,2]
    result = solution.getSneakyNumbers(nums)
    print("Sneaky Numbers:", result)
        
if __name__ == "__main__":
    main()
