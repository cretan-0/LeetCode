class Solution(object):
    def sortArrayByParity(self, nums):
        even = []
        odd = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd

def main():
    sol = Solution()
    nums = [3, 1, 7, 9, 2, 9, 6, 10]
    print(sol.sortArrayByParity(nums))

if __name__ == "__main__":
    main()
