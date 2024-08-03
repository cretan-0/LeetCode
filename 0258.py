# 0258. Add Digits
class Solution(object):
    def addDigits(self, num):
        res = 0
        while num:
            digits = [int(x) for x in str(num)]
            res = sum(digits)
            #print(res)
            num = res
            if num < 10:
                break
        return num

def main() -> None:
    sol = Solution()
    num = 38
    print(sol.addDigits(num))

if __name__ == "__main__":
    main()
