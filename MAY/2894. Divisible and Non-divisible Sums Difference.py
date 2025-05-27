class Solution(object):
    def differenceOfSums(self, n, m):
        num1 = 0
        num2 = 0
        for elem in range(1, n+1):
            if elem % m != 0:
                num1 += elem
            else:
                num2 += elem
        return num1 - num2
