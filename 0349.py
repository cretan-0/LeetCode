class Solution(object):
    def intersection(self, nums1, nums2):
        res = []
        for i, j in zip(nums1, nums2):
            if i in nums1 and i in nums2 and i not in res:
                res.append(i)
            if j in nums1 and j in nums2 and j not in res:
                res.append(j)
        return res

# V2

class Solution(object):
    def intersection(self, nums1, nums2):
        res = []
        for i in nums1:
            if i in nums2 and i not in res:
                res.append(i)
        return res
