class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums = nums1 + nums2
        res = []
        for num in nums:
            if num != 0:
                res.append(num)
        return sorted(res)



def main() -> None:
    solution = Solution()
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(solution.merge(nums1, m, nums2, n))


if __name__ == "__main__":
    main()