class Solution(object):
    def targetIndices(self, nums, target):
        listNumber = []
        nums.sort()
        for i, num in enumerate(nums):
            if num == target:
                listNumber.append(i)
        return listNumber


def main() -> None:
    solution = Solution()
    nums = [1,2,5,2,3]
    target = 2
    print(solution.targetIndices(nums, target))

main()