from collections import Counter
class Solution(object):
    def frequencySort(self, nums):
        r = Counter(nums).most_common()

        r.sort(key=lambda x: x[0], reverse=True)
        r.sort(key=lambda x: x[1])

        new_arr = []
        for i in r:
            new_arr += ([i[0]] * i[1])
        return new_arr


def main() -> None:
    sol = Solution()
    nums = [-1,1,-6,4,5,-6,1,4,1]
    print(sol.frequencySort(nums))

if __name__ == "__main__":
    main()

