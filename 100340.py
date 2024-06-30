class Solution(object):
    def maxHeightOfTriangle(self, red, blue):
        row = 0
        while blue >= 1 and red >= 1:
            row += 1
            if row % 2 == 1:
                red -= row
            if row % 2 == 0:
                blue -= row
        return row



'''
        row = 0
        r = blue + red
        while r > 1:
            row += 1
            r -= row
        return row
'''


def main() -> None:
    sol = Solution()
    red = 10
    blue = 1
    print(sol.maxHeightOfTriangle(red, blue)) # out: 3 -> exp: 4

if __name__ == "__main__":
    main()
