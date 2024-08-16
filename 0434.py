class Solution(object):
    def countSegments(self, s):
        if len(s) == 0:
            return 0
        else:
            s = s.split()
            return len(s)

def main() -> None:
    sol = Solution()
    s = "Hello, my name is John"
    print(sol.countSegments(s))

if __name__ == "__main__":
    main()

