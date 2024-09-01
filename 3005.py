from collections import Counter

class Solution(object):
    def maxFrequencyElements(self, nums):
        z = Counter(nums)
        max = -100000
        for num in z.values():
            if num > max:
                max = num
        counter = 0
        for key, value in z.items():
            if value == max:
                counter+=1
        return counter * max


def main() -> None:
    sol = Solution()
    nums = [1, 2, 2,3,1,4]
    print(sol.maxFrequencyElements(nums))

if __name__ == "__main__":
    main()
