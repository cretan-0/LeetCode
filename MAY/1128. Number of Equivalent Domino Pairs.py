import types
from collections import Counter
class Solution:
    def numEquivDominoPairs(self, dominoes) -> int: # aici valoarea returnata trebuie sa fie un int
        dominoes = sorted([tuple(sorted(domino)) for domino in dominoes])
        count = Counter(dominoes)
        res = 0
        for val in count.values():
            if val > 1:
                res += val * (val-1) // 2

        return res



def main() -> None: # functia nu returneaza nimic, acest "None" este pus explicit
    dominoes = [[1,2],[2,1],[3,4],[5,6]]
    print(Solution().numEquivDominoPairs(dominoes))




if __name__ == "__main__":
    main()

'''
We have Permutations and Combinations.
Permutation (order matters):
a, b, c: ab, ba, ac, ca, bc, cb
Combinations (order does not matter):
a, b, c: ab, bc, ac
This problem is a Combinations problem
Formula for Combinations:
C(n,r) = n!/( r! (n - r)! )

Simplifying for r = 2:
C(n, 2) = n*(n-1)/2
'''