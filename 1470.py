class Solution(object):
    def shuffle(self, nums, n):
        res1 = []
        res2 = []
        result = []
        for i in range(n):
            res1.append(nums[i])

        allElements = 2 * n

        for j in range(n, allElements):
            res2.append(nums[j])

        for i in range(n):
            result.append(res1[i])
            result.append(res2[i])
        return result


def main():
    solution = Solution()  #  se creaza o instanta a clasei Solution()
    nums = [2, 5, 1, 3, 4, 7]
    n = 3
    print(solution.shuffle(nums,n))  #  Se apelezeaza medota shuffle asupra instantei solution

main()