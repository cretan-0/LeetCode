# V1

class Solution(object):
    def myPow(self, x, n):
        return x**n
		
# V2
class Solution(object):
    def myPow(self, x, n):
        return pow(x,n)
		
# V3: 291 / 307 testcases passed -> Time Limit Exceeded

class Solution(object):
    def myPow(self, x, n):
        result = 1
        if n == 0:
            return 1
        if x == 0:
            return 0
        if n < 0:
            return x ** n
        while n>0:
            result = result * x
            n-=1
        return result

def main() -> None:
    solution = Solution()
    x = 0.00001
    n = 2147483647
    print(solution.myPow(x, n))

if __name__ == '__main__':
    main()