import types
from collections import Counter
class Solution:
    def numEquivDominoPairs(self, dominoes) -> int: # aici valoarea returnata trebuie sa fie un int
        dominoes = sorted([tuple(sorted(domino)) for domino in dominoes])
        a = Counter(dominoes)
        return max(a.values()-1)


def main() -> None: # functia nu returneaza nimic, acest "None" este pus explicit
    dominoes = [[1,2],[2,1],[3,4],[5,6]]
    print(Solution().numEquivDominoPairs(dominoes))

if __name__ == "__main__":
    main()
