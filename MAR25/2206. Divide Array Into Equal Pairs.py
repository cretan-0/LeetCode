from collections import Counter
class Solution(object):
    def divideArray(self, nums):
        hashmap = Counter(nums)
        equal_pairs = True
        for elem in hashmap.values():
            if elem % 2 == 1:
                equal_pairs = False
        return equal_pairs
        
