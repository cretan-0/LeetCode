#V1 -> Memory Limit Exceeded
class Solution(object):
    def checkPerfectNumber(self, num):
        res = 0
        for i in range(1, num):
            if num % i == 0:
                res += i
        return res == num


def main() -> None:
    num = 30402457
    sol = Solution()
    print(sol.checkPerfectNumber(num))

if __name__ == "__main__":
    main()
