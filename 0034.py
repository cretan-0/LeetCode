class Solution(object):
    def searchRange(self, nums, target):
        counter = nums.count(target)
        if counter == 0:
            return [-1, -1]
        elif counter == 1:
            index = nums.index(target)
            return [index, index] # or [index] * 2
        else:
            res = []
            revNums = nums[::-1]
            min_index = -1
            max_index = 0
            for i, num in enumerate(nums):
                if num == target:
                    min_index = i
                    break
            for j, num in enumerate(revNums):
                if nums[j] == target:
                    max_index = j
            res.append(min_index)
            res.append(max_index)
            return res
"""
# a short and compact version (runtime is bigger than the previous version)
class Solution(object):
    def searchRange(self, nums, target):
        list_of_index = []
        for i, num in enumerate(nums):
            if nums[i] == target:
                list_of_index.append(i)
        if len(list_of_index) == 0:
            return [-1, -1]
        elif len(list_of_index) == 1:
            return list_of_index*2
        else:
            return [min(list_of_index), max(list_of_index)]
"""
