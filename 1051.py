class Solution(object):
    def heightChecker(self, heights):
        copy_heights = heights
        heights = sorted(heights)
        counter = 0
        for num in range(len(heights)):
            if copy_heights[num] != heights[num]:
                counter+=1
        return counter



def main() -> None:
    sol = Solution()
    heights = [1,2,3,4,5]
    print(sol.heightChecker(heights))

if __name__ == "__main__":
    main()

