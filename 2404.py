# https://leetcode.com/problems/most-frequent-even-element/description/
class Solution(object):
    def mostFrequentEven(self, nums):
        hashtable = {}
        index = 0
        counterEven = 0
        for num in sorted(nums):
            if num % 2 == 0:
                counterEven += 1
        if counterEven == 0:
            return -1
        for num in nums:
            if num in hashtable and num % 2 == 0:
                hashtable[num] += 1
            elif num not in hashtable and num % 2 == 0:
                hashtable[num] = 1
            else:
                pass
        print(hashtable)
        maxVal = max(hashtable.values()) 
        print(maxVal)
        for key, value in sorted(hashtable.items()):
            if value == maxVal:
                index = key
                break
        return index

def main() -> None:
    solution = Solution()
    nums = [0,1,2,2,4,4,1]
    print(solution.mostFrequentEven(nums))

if __name__ == '__main__':
    main()