class Solution(object):
    def searchRange(self, nums, target):
        res = []
        length_res = len(res)
        counter = nums.count(target)
        if counter == 0:
            result = [-1, -1]
            return result
        elif counter == 1:
            index = nums.index(target)
            result = [target, target]
            return result
        else:
            min_index = 10000000
            max_index = -10000000
            for i, num in enumerate(nums):
                if num == target and num < min_index:
                    min_index = i
                if num == target and num > max_index:
                    max_index = i
            res.append(min_index)
            res.append(max_index)
            return res