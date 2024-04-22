# Python
class Solution(object):
    def findNumbers(self, nums):
        counterEven = 0
        for num in nums:
            counterCycles = 0
            while num != 0:
                counterCycles += 1
                num //= 10
            if counterCycles % 2 == 0:
                counterEven += 1
        return counterEven
        
# Python3

class Solution(object):

    res = 0

    def isEven(num):
        return num % 2 ==0
    def findNumbers(self, nums):
        counterNumEven = 0
        for num in nums:
            digits = 0
            while num > 0:
                num //= 10
                digits += 1
            if Solution.isEven(digits):
                self.res += 1
        return self.res


def main() -> None:
    solution = Solution()
    nums = [555, 901, 482, 1771]
    print(solution.findNumbers(nums))

if __name__ == '__main__':
    main()
        