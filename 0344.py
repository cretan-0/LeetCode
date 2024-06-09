class Solution(object):
    def reverseString(self, s):
        s.reverse()
        return s

    # s[::-1] will return a reverse string, but won't change the initial string

def main() -> None:
    sol = Solution()
    s = ["h", "e", "l", "l", "o"]
    print(sol.reverseString(s))

if __name__ == "__main__":
    main()

# Time complexity O(n)
# Space complexity O(1)

# smart version
class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(n//2): # parcurgem stringul pana la jumatate
            s[i], s[n-1-i] = s[n-1-i], s[i] # swap intre primul element si ultimul element iterativ ;)

# Time complexity O(n)
# Space complexity O(1)

# another smart version
class Solution(object):
    def reverseString(self, s):
        left = 0
        right = len(s)-1
        while (left < right):
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left +=1
            right -= 1
        return s
