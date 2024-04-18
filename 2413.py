class Solution(object):
    def smallestEvenMultiple(self, n):
        if n % 2 == 0:
            return n
        return n * 2

def main():
    solution = Solution()
    n = 5
    print(solution.smallestEvenMultiple(n))

main()