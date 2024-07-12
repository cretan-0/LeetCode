class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for char in magazine:
            ransomNote = ransomNote.replace(char, '', 1)
        return ransomNote == ''





def main() -> None:
    sol = Solution()
    ransomNote = "aa"
    magazine = "aab"
    print(sol.canConstruct(ransomNote,magazine))


if __name__ == "__main__":
    main()
