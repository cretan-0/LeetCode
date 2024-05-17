class Solution(object):
    def interchangeableRectangles(self, rectangles):
        counter = 0
        n = len(rectangles)
        for i in range(len(rectangles)-1):
            for j in range(i + 1, n):
                if (rectangles[i][0] / rectangles[i][1]) == (rectangles[j][0] / rectangles[j][1]):
                    counter += 1
        return counter

def main() -> None:
    sol = Solution()
    rectangles = [[1,7],[2,8],[8,8],[2,5],[2,8],[7,4]]
    print(sol.interchangeableRectangles(rectangles))


if __name__ == "__main__":
    main()

