# https://leetcode.com/problems/majority-element-ii/
class Solution(object):
    def noContainsDuplicates(self, nums):
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return False
        return True
    def majorityElement(self, nums):
        hashtable = {}
        index = []
        if self.noContainsDuplicates(nums):
            return nums
        for num in nums:
            if num in hashtable:
                hashtable[num] += 1
            else:
                hashtable[num] = 1
        print(hashtable)
        if hashtable:
            maxVal = max(hashtable.values())
            for key, value in hashtable.items():
                if maxVal == value:
                    index.append(key)
                    break
        return index

def main() -> None:
    solution = Solution()
    nums = [3,2,3]
    print(solution.majorityElement(nums))

if __name__ == '__main__':
    main()