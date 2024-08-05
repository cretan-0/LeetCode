# Runtime: 252ms, Beats 16.37%
# Memory: 11.81MB, Beats 90.06

class Solution(object):
    def kthDistinct(self, arr, k):
        new_arr = []
        for num in arr:
            if arr.count(num) < 2:
                new_arr.append(num)
        if len(new_arr) < k:
            return ""
        else:
            return new_arr[k-1]


def main() -> None:
    sol = Solution()
    arr = ["aaa","aa","a"]
    k = 1
    print(sol.kthDistinct(arr, k))

if __name__ == "__main__":
    main()

