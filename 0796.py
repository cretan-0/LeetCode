class Solution(object):
    def rotateString(self, s, goal):
        for i in range(len(s)):
            goal = goal[1:] + goal[:1]
            print(goal)
            if s == goal:
                return True
        return False

def main() -> None:
    sol = Solution()
    s = "abcde"
    goal = "cdeab"
    print(sol.rotateString(s, goal))

if __name__ == "__main__":
    main()