class Solution(object):
    def getNoZeroIntegers(self, n):
        res = []
        for i in range(n):
            if '0' in str(i) or '0' in str(n-i):
                continue
            return [i, n-i]

        
