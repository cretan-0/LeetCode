from typing import List
from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = sorted(s1.split())
        s2 = sorted(s2.split())
        all_words = s1 + s2
        count_word = Counter(all_words)
        return [word for word in count_word if count_word[word] == 1]


def main() ->  None:
    sol = Solution()
    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    print(sol.uncommonFromSentences(s1, s2))


if __name__ == "__main__":
    main()
