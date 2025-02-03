class Solution(object):
    def longestMonotonicSubarray(self, nums):
        set_nums = set(nums)
        if len(set_nums) == 0:
            return 1

        cnt_i = 0
        cnt_d = 0
        i = j = 0
        while i < len(nums)-1:
            if nums[i] > nums[i+1]:
                cnt_i += 1

            else:
                res_i = cnt_i
                cnt_i = max(cnt_i, res_i)
            i+=1

        while j < len(nums)-1:
            if nums[j] < nums[j+1]:
                cnt_d += 1
            else:
                res_d = cnt_d
                cnt_d = max(cnt_d, res_d)
            j+=1
        
        return max(cnt_i, cnt_d)

def main() -> None:
    sol = Solution()
    nums = [3,2,1]
    print(sol.longestMonotonicSubarray(nums))


if __name__ == "__main__":
    main()
