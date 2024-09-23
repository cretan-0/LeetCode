from typing import List
from collections import Counter


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        all_s1 = Counter(words1)
        all_s2 = Counter(words2)
        counter = 0
        for elem in all_s1:
            if elem in all_s2 and all_s1[elem] == all_s2[elem] == 1:
                counter += 1
        return counter






def main() ->  None:
    sol = Solution()
    words1 = ["leetcode","is","amazing","as","is"]
    words2 = ["amazing","leetcode","is"]
    print(sol.countWords(words1, words2))


if __name__ == "__main__":
    main()
