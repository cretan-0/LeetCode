import textwrap
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        width = 1
        list_jewels = []
        counter = 0
        list_jewels = textwrap.wrap(jewels, width)
        list_stones = textwrap.wrap(stones, width)
        for elem in list_stones:
            if str(elem) in list_jewels:
                counter += 1
        return counter

def main():
    sol = Solution()
    jewels = "aA"
    stones = "aAAbbbb"
    print(sol.numJewelsInStones(jewels, stones))


if __name__ == "__main__":
    main()