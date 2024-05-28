class Solution(object):
    def isArraySpecial(self, nums, queries):
        res = []
        for i in range(len(queries)):
            index1 = queries[i][0]
            index2 = queries[i][1]
            ver_adjacent_parity = True
            for j in range(index1, index2):
                if (nums[j] % 2 == 0 and nums[j+1] % 2 == 0) or (nums[j] % 2 == 1 and nums[j+1] % 2 == 1):
                    ver_adjacent_parity = False
            res.append(ver_adjacent_parity)
        return res

def main() -> None:
    sol = Solution()
    nums = [4, 3, 1, 6]
    queries = [[0, 2], [2, 3]]
    print(sol.isArraySpecial(nums, queries))


if __name__ == "__main__":
    main()
