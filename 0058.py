# Python3

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strS = s.rstrip().split()
        return len(strS[-1])

# Python

class Solution(object):
    def lengthOfLastWord(self, s):
        strS = s.rstrip().split()
        strS.reverse()
        return len(strS[0])

def main():
    solution = Solution()
    s = "luffy is still joyboy"
    print(solution.lengthOfLastWord(s))

main()