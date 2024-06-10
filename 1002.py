from collections import Counter
class Solution(object):
    def commonChars(self, words):
        freq = Counter(words[0])
        for word in words:
            new_freq = Counter(word)
            freq = freq & new_freq
        res = []
        for c, f in freq.items():
            res += c * f
        return res


def main() -> None:
    sol = Solution()
    words = ["bella", "label", "roller"]
    print(sol.commonChars(words))

if __name__ == "__main__":
    main()
