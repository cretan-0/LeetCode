class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        res = [] # res = {} -> in case of dictionary
        for i in range(len(nums)):
            counter = 0
            for j in range(1, len(nums)):
                if nums[i] > nums[j]:
                    counter+=1
            res.append(counter)
        return res
            # res[i] = counter -> in case of dictionary
        #return list(res.values()) -> in case of dictionary


def main():
    solution = Solution()
    nums = [8,1,2,2,3]
    print(solution.smallerNumbersThanCurrent(nums))

main()