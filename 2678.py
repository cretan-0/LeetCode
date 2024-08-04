'''
# another apporach

class Solution(object):
    def countSeniors(self, details):
        return sum (int(x[11:13]) > 60 for x in details)
'''

# Runtime: 32ms, 8.98%
# Memory: 11.70MB, 49.54%

class Solution(object):
    def countSeniors(self, details):
        count = 0
        for elem in details:
            res = elem[11:13]
            if int(res) > 60:
                count +=1
        return count


def main() -> None:
    sol = Solution()
    details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
    print(sol.countSeniors(details))

if __name__ == "__main__":
    main()

