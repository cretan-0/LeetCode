import math
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""
        max_length = math.gcd(len(str1), len(str2))
        return str1[:max_length]

def main() -> None:
    sol = Solution()
    str1 = "ABABAB"
    str2 = "ABAB"
    print(sol.gcdOfStrings(str1, str2))

if __name__ == "__main__":
    main()
