# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/solutions/5587104/python-runtime-55ms-64-19-memory-11-65mb-beats-93-92/
# Runtime: 55ms, 64.19%
# Memory: 11.65MB, Beats 93.92%

class Solution(object):
    def canBeEqual(self, target, arr):
        return sorted(target) == sorted(arr)



def main() -> None:
    sol = Solution()
    target = [1,2,3,4]
    arr = [2,4,1,3]
    print(sol.canBeEqual(target, arr))

if __name__ == "__main__":
    main()
