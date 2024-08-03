class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        num_indices = {}
        for cur_idx, cur_num in enumerate(nums):
            if cur_num in num_indices:
                if abs(cur_idx - num_indices[cur_num]) <= indexDiff and abs(nums[cur_idx] - nums[num_indices[cur_num]]) <= valueDiff:
                    print("i")
                print(abs(cur_idx - num_indices[cur_num]))
                print("-----")
                print(abs(nums[cur_idx] - nums[num_indices[cur_num]]) <= valueDiff)
                print("****")
                print(nums[cur_idx])
                print("+++++")
                print(nums[num_indices[cur_num]])
                #    return True
            num_indices[cur_num] = cur_idx

        return False


def main() -> None:
    sol = Solution()
    nums = [8,7,15,1,6,1,9,15]
    indexDiff = 1
    valueDiff = 3
    print(sol.containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff))

if __name__ == "__main__":
    main()
