class Solution(object):
    def isPowerOfTwo(self, n):
        for i in range(0, 31):
            if n == pow(2,i):
                return True
        return False
