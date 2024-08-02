class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        num_indices = {}
        for current_idx, curr_num in enumerate(nums):
            if curr_num in num_indices:
                if current_idx - num_indices[curr_num] <= k:
                    return True
            num_indices[curr_num] = current_idx

        return False


'''
#  time exceed at big data -> try hashtable

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        for i in range(len(nums)):
            print(f'i=', {i})
            for j in range(1, len(nums)):
                print(f'j:', {j})
                if nums[i] == nums[j]  and abs(i-j) <= k:
                    return True

'''
