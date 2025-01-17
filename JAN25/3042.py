class Solution(object):
    def countPrefixSuffixPairs(self, words):
        cnt = 0
        for i in range(len(words) - 1):
            l = len(words[i])
            for j in range(i, len(words)):
                l2 = len(words[j])
                print(words[j][:l], words[j][:])
                if words[j][:l] == words[i] and words[j][l2:] == words[i]:
                    cnt += 1
        return cnt


def main() -> None:
    sol = Solution()
    words = ["a", "aba", "ababa", "aa"]
    print(sol.countPrefixSuffixPairs(words))


if __name__ == "__main__":
    main()
