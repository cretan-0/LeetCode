# https://leetcode.com/problems/sort-the-people/solutions/5593574/python-runtime-77ms-beats-79-77-memory-12-15mb-73-10/
# Runtime: 77ms, Beats 79.77%
# Memory: 12.15MB, 73.10%

class Solution(object):
    def sortPeople(self, names, heights):
        hashtable = {}
        for i, item in enumerate(heights):
            if item in hashtable:
                hashtable[item] += names[i]
            else:
                hashtable[item] = names[i]

        hashtable = sorted(hashtable.items(), reverse=True)
        
        new_arr = []
        
        for i in hashtable:
            new_arr.append(i[1])
        return new_arr


def main() -> None:
    sol = Solution()
    names = ["Mary","John","Emma"]
    heights = [180,165,170]
    print(sol.sortPeople(names, heights))

if __name__ == "__main__":
    main()

