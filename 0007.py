class Solution(object):
    def reverse(self, x):
        sign = -1
        cpX = x
        if cpX < 0:
            x = x * sign
        reverseX = 0
        while x:
            reverseX = reverseX * 10 + x % 10
            x = x // 10
        if reverseX < -2**31-1 or reverseX > 2**31-1:
            return 0
        return reverseX if cpX > 0 else reverseX * sign

def main() -> None:
    solution = Solution()
    x = -123
    print(solution.reverse(x))

if __name__ == '__main__':
    main()