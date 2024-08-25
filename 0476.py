class Solution(object):
    def findComplement(self, num):
        a = str(bin(num))
        a = a[2:]
        a = a.replace('0', '7')
        a = a.replace('1', '0')
        a = a.replace('7', '1')
        return (int(a, 2))


def main() -> None:
    sol = Solution()
    num = 5
    print(sol.findComplement(num))

if __name__ == "__main__":
    main()
