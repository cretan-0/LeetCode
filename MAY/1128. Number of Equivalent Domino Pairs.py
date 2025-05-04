import types
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int: # aici valoarea returnata trebuie sa fie un int
        pass


def main() -> None: # functia nu returneaza nimic, acest "None" este pus explicit
    dominoes = [[1,2],[2,1],[3,4],[5,6]]
    print(Solution().numEquivDominoPairs(dominoes))

if __name__ == "__main__":
    main()
