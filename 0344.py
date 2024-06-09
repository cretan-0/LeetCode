class Solution(object):
    def reverseString(self, s):
        s.reverse()
        return s

    # s[::-1] will return a reverse string, but won't change the initial string

def main() -> None:
    sol = Solution()
    s = ["h", "e", "l", "l", "o"]
    print(sol.reverseString(s))

if __name__ == "__main__":
    main()

# smart version
class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(n//2):
            s[i], s[n-1-i] = s[n-1-i], s[i]
