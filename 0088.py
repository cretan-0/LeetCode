class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[m:] = nums2
        return sorted(nums1)


def main() -> None:
    sol = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print(sol.merge(nums1, m, nums2, n))

if __name__ == "__main__":
    main()
