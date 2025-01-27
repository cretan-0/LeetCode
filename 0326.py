class Solution(object):
    def isPowerOfThree(self, n):
        for i in range(0, 31):
            if n == pow(3,i):
                return True
        return False
