import re
class Solution(object):
    def isPalindrome(self, s):
        s = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        reverseS = s[::-1]
        return s == reverseS


def main() -> None:
    solution = Solution()
    s = ".a"
    print(solution.isPalindrome(s))

if __name__ == '__main__':
    main()