# https://leetcode.com/problems/reverse-prefix-of-word/description/?envType=daily-question&envId=2024-05-01

# correct version

class Solution(object):
    def reversePrefix(self, word, ch):
        counter = 0
        for char in word:
            if char == ch:
                counter += 1
        if counter == 0:
            return word
        elif len(word) == counter:
            return word
        else:
            index = 0
            prefix = ''
            for i, char in enumerate(word):
                if char in word and char == ch:
                    index = i
                    break
            prefix = word[:index+1]
            suffix = word[index+1:len(word)]
           # print(index)
           # print(prefix)
           # print(suffix)
            return prefix[::-1] + suffix



"""
V2: incorrect
class Solution(object):
    def reversePrefix(self, word, ch):
        if ch not in word:
            return word
        else:
            start = word.split()
            print("start:", start)

            copy_start = start[:]
            del copy_start[0]
            after_ch = "".join(copy_start)
            print(after_ch)
            start[0] = start[0] + ch
            res = start[0][::-1]
            print(res)
            return res + after_ch



def main() -> None:
    solution = Solution()
    word = "abcdefd"
    ch = "d"
    print(solution.reversePrefix(word, ch))

if __name__ == "__main__":
    main()
"""

"""
V3: incorrect

class Solution(object):
    def reversePrefix(self, word, ch):
        counter = 0
        for char in word:
            if char == ch:
                counter += 1

        if ch not in word:
            return word
        elif len(word) == counter:
                return word
        else:
            start = word.split(ch)
            start[0] += ch
            if '' in start:
                start.append(ch)
            print(start)
            prefix = start[0][::-1]
            print("prefix: ", prefix)
            del start[0]
            print(start)
            res = "".join(start)
            print(res)
            ver = len(res)
            if len(res) <= 1:
                return prefix
            else:
                return prefix+res
"""

"""
# V4: incorrect
class Solution(object):
    def reversePrefix(self, word, ch):
        counter = 0
        for char in word:
            if char == ch:
                counter += 1
        if counter == 0:
            return word
        elif len(word) == counter:
            return word
        else:
            word = word.split(ch)
            print("word: ",word)
            prefix_after_split = word[0] + ch
            print("word[0] + ch: ", word[0] + ch)
            del word[0]
            if '' in word:
                word.append(ch)
            print("prefix: ", prefix_after_split[::-1])
            suffix_of_word = "".join(word)
            print("suffix: ", suffix_of_word)
            return prefix_after_split[::-1] + suffix_of_word

"""