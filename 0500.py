class Solution(object):
    def findWords(self, words):
        keyboad_1 = "qwertyuiop"
        keyboad_2 = "asdfghjkl"
        keyboad_3 = "zxcvbnm"
        res = []
        for word in words:
            counter_k1 = 0
            counter_k2 = 0
            counter_k3 = 0
            for char in word.lower():
                if char in keyboad_1:
                    counter_k1 += 1
                elif char in keyboad_2:
                    counter_k2 += 1
                elif char in keyboad_3:
                    counter_k3 += 1
            if counter_k1 == len(word) or counter_k2 == len(word) or counter_k3 == len(word):
                res.append(word)
        return res


def main():
    solution = Solution()
    words = ["adsdf","sfd"]
    print(solution.findWords(words))

if __name__ == "__main__":
    main()