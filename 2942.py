class Solution(object):
    def findWordsContaining(self, words, x):
        list_index = []
        i = 0
        for word in words:
            if x in word:
                list_index.append(i)
            i += 1
        return list_index


def main() -> None:
    solution = Solution()
    words = ["abc","bcd","aaaa","cbc"]
    x = "z"
    print(solution.findWordsContaining(words, x))

main()