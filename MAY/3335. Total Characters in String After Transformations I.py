'''
Time Limit Exceeded
502 / 824 testcases passed
Last Executed Input
Use Testcase
s =
"jqktcurgdvlibczdsvnsg"
t =
7517
'''

class Solution(object):
    def lengthAfterTransformations(self, s, t):
        # creating a list of all letters from alphabet
        alpha = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        res = ''
        temp = s
        while t:
            res=''
            for char in temp:
                index = alpha.index(char)
                if index < len(alpha) - 1:
                    res += alpha[index + 1]
                if alpha[index] == 'z':
                    res += 'ab'
            temp = res
            print(temp)
            t -= 1
        return res


def main() -> None:
    s = "abcyy"
    t = 2
    print(Solution().lengthAfterTransformations(s, t))


if __name__ == "__main__":
    main()
