class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in s:
            t = t.replace(char, '',1)
        return t


def main() -> None:
    sol = Solution()
    s = "abcd"
    t = "abcde"
    print(sol.findTheDifference(s, t))


if __name__ == "__main__":
    main()
