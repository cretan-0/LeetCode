class Solution(object):
    def majorityElement(self, nums):
        hashtable = {}
        index = 0
        for num in nums:
            if num in hashtable:
                hashtable[num] += 1
            else:
                hashtable[num] = 1
        maxVal = max(hashtable.values()) # max = 4, but i need index of 4
        for key, value in hashtable.items():
            if value == maxVal:
                index = key
                break
        return index