class Solution(object):
    def maxScore(self, s):
        counter_max = 0
        for i in range(len(s)-1):
            left = s[:i+1]
            right = s[i+1:]
            counter_max = max(counter_max, left.count('0') + right.count('1')) 
        return counter_max


def main() -> None:
    sol = Solution()
    s = "1111"
    print(sol.maxScore(s))


if __name__ == "__main__":
    main()
