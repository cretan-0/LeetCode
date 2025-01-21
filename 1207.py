class Solution(object):
    def uniqueOccurrences(self, arr):
        hashset = {}
        for i, elem in enumerate(arr):
            if elem in hashset:
                hashset[elem] +=1
            else:
                hashset[elem] = 1

        len_bef = len(hashset)

        a = set(hashset.values())

        len_aft = len(a)

        return len_bef == len_aft


def main() -> None:
    sol = Solution()
    arr = [1,2,2,1,1,3]
    print(sol.uniqueOccurrences(arr))


if __name__ == "__main__":
    main()
