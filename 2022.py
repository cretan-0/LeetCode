class Solution(object):
    def construct2DArray(self, original, m, n):
        res = []
        if len(original) != m*n:
            return []
        else:
            for i in range(0, len(original), n):
                res.append(original[i:i+n])
        return res

def main() -> None:
    sol = Solution()
    original = [1, 2, 3,4]
    m = 2
    n = 2
    print(sol.construct2DArray(original, m, n))

if __name__ == "__main__":
    main()
