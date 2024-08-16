class Solution(object):
    def maxDistance(self, arrays):
        minim = arrays[0][0]
        maxim = arrays[0][-1]
        res = 0
        for arr in arrays[1:]:
            start = arr[0]
            end = arr[-1]
            res = max(end-minim, maxim-start, res)
            minim = min(minim, start)
            maxim = max(maxim, end)
        return res




def main() -> None:
    sol = Solution()
    arrays = [[1, 2, 3], [4, 5], [1, 2, 3,4 ]]
    #arrays = [[1],[2]]
    #arrays = [[1,4],[0,5]]
    #arrays = [[-1,1],[-3,1,4],[-2,-1,0,2]]
    print(sol.maxDistance(arrays))

if __name__ == "__main__":
    main()
