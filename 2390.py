class Solution(object):
    def removeStars(self, s):
        stack = []
        for char in s:
            if stack and char == "*":
                stack.pop()
            else:
                stack.append(char)
        return stack


def main() -> None:
    solution = Solution()
    s = "leet**cod*e"
    print(solution.removeStars(s))

if __name__ == "__main__":
    main()