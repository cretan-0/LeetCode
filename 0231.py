class Solution(object):
    def isPowerOfFour(self, n):
        for i in range(0, 30):
            if n == pow(2,i):
                return True
        return False
