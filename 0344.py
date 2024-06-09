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
