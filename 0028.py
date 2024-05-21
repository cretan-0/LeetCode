class Solution(object):
    def strStr(self, haystack, needle):
        len_needle = len(needle)
        for i in range(len(haystack)):
            if needle == haystack[i:len_needle]:
                return i
            len_needle= len_needle + 1
        return -1

def main() -> None:
    sol = Solution()
    haystack = "hello"
    needle = "ll"
    print(sol.strStr(haystack, needle))

if __name__ == "__main__":
    main()