"""
# version with constraints
class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        counter = 0
        if len(arr) >= 3 and len(arr) <= 100 and a >= 0 and a <= 1000 and b >=0 and b <= 1000 and c >= 0 and c <= 1000:
            for i in range(len(arr)):
                for j in range(len(arr)):
                    for k in range(len(arr)):
                        if 0 <= i < j < k < len(arr) and abs(arr[i] - arr[j]) <= a \
                                and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            counter += 1
                            print(arr[i], arr[j], arr[k])
            return counter

"""


class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        counter = 0
        for i in range(len(arr)):
            for j in range(len(arr)):
                for k in range(len(arr)):
                    if 0 <= i < j < k < len(arr) and abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        counter += 1
        return counter



def main() -> None:
    sol = Solution()
    arr = [3,0,1,1,9,7]
    a = 7
    b = 2
    c = 3
    print(sol.countGoodTriplets(arr, a, b, c))

if __name__ == "__main__":
    main()
    
'''
# fastest version
class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        counter = 0
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):  
                if abs(arr[i] - arr[j]) > a:  
                    continue
                for k in range(j + 1, n):  
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:  
                        counter += 1
        return counter
'''

