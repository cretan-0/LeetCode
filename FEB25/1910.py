class Solution(object):
    def removeOccurrences(self, s, part):
        while part in s:
            s = s.replace(part, "", 1) # delete only first occurance
        return s


#v2
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while True:
            idx = s.find(part)
            if idx == -1:
                break
            s = s[:idx] + s[idx + len(part):]
            print(s)
        return s

def main() -> None:
    sol = Solution()
    s = "daabcbaabcbc"
    part = "abc"
    print(sol.removeOccurrences(s, part))

if __name__ == "__main__":
    main()
