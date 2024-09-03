class Solution(object):
    def getLucky(self, s, k):
        sum = 0
        a = 0
        for string in s:
            a = (ord(string)) - 96
            digits = [int(digit) for digit in str(a)]
            for dig in digits:
                sum += dig
        res = 0
        if k < 2:
            return sum
        else:
            k-=1
            while k:
                k-=1
                res = 0
                digits = [int(digit) for digit in str(sum)]
                for s in digits:
                    res += s
                sum = res
        return res




def main() -> None:
    sol = Solution()
    s = "leetcode"
    k = 2
    print(sol.getLucky(s, k))

if __name__ == "__main__":
    main()
