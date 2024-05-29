class Solution(object):
    def findPermutationDifference(self, s, t):
        counter = 0
        for i in range(len(s)):
            sum = 0
            for j in range(len(t)):
                if s[i] == t[j]:
                    sum = abs(i-j)
                    print(i, " ", j)
            counter+=sum
        return counter

def main() -> None:
    sol = Solution()
    s = "abcde"
    t = "edbac"
    print(sol.findPermutationDifference(s, t)) # 12



if __name__ == "__main__":
    main()
