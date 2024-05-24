class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

# V2

class Solution(object):
    def containsDuplicate(self, nums):
        hashtable = {}
        for num in nums:
            if num in hashtable:
                hashtable[num] += 1
            else:
                hashtable[num] = 1
        if max(hashtable.values()) > 1:
            return True
        else:
            return False

def main() -> None:
    sol = Solution()
    nums = [1,2,3,4]
    print(sol.containsDuplicate(nums))


if __name__ == "__main__":
    main()
