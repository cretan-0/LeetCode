
#  time exceed at big data -> try hashtable

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        for i in range(len(nums)):
            print(f'i=', {i})
            for j in range(1, len(nums)):
                print(f'j:', {j})
                if nums[i] == nums[j]  and abs(i-j) <= k:
                    return True

