class Solution(object):
    def countPrimeSetBits(self, left, right):
        primeNumList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        interval = range(left,right+1)
        listNumber = list(interval)
        counter = 0
        for num in listNumber:
            z = bin(num).count("1")
            if z in primeNumList:
                counter+=1
            z = 0
        return counter