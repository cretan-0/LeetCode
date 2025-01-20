from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        result = []
        for num in count1:
            result.extend([num] * min(count1[num], count2.get(num, 0)))
        
        return result
