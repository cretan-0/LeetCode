from collections import Counter
class Solution(object):
    def hammingWeight(self, n):
        n = bin(n)
        n = Counter(n)
        return n['1']
