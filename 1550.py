class Solution(object):
    def threeConsecutiveOdds(self, arr):
        for i in range(2,len(arr)):
            if arr[i-2] % 2 == 1 and arr[i-1] % 2 == 1 and arr[i] % 2 == 1:
                return True
        return False
        
# v2

v
class Solution(object):
    def threeConsecutiveOdds(self, arr):
        count = 0
        for elem in arr:
            if elem % 2 == 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False


def main() -> None:
    sol = Solution()
    arr = [1,2,34,3,4,5,7,23,12]
    print(sol.threeConsecutiveOdds(arr))


if __name__ == "__main__":
    main()
