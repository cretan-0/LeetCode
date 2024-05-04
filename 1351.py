# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/

class Solution(object):
    def countNegatives(self, grid):
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    counter += 1
        return counter

def main() -> None:
    solution = Solution()
    grid = [[5,1,0],[-5,-5,-5]]
    print(solution.countNegatives(grid))

if __name__ == "__main__":
    main()

"""
# version2.0

class Solution(object):
    def countNegatives(self, grid):
        counter = 0
        for i in grid:
            for j in i:
                if j < 0:
                    counter += 1
        return counter
"""
