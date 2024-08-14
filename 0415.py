class Solution(object):
    def addStrings(self, num1, num2):
        rez = int(num1) + int(num2)
        return str(rez)

#v2
class Solution(object):
    def addStrings(self, num1, num2):
        return str(int(num1)+int(num2))


def main() -> None:
    sol = Solution()
    num1 = "11"
    num2 = "123"
    print(sol.addStrings(num1, num2))

if __name__ == "__main__":
    main()
