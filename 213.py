class Solution(object):
    def isPowerOfTwo(self, n):
        if n % 2 == 0:
            return True
        elif n == 1:
            return True
        else:
            return False
        