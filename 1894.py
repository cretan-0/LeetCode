class Solution(object):
    def chalkReplacer(self, chalk, k):
        while k:
            ans = 0
            l = 0
            r = len(chalk)-1
            while l <= r:
                k -= chalk[l]
                if k == 0:
                    return l
                if k < 0:
                    return l
                l += 1
                if l > r:
                    l = 0
                print(k)
            return ans


def main() -> None:
    sol = Solution()
    chalk = [5,1,5]
    k = 22
    print(sol.chalkReplacer(chalk, k))

if __name__ == "__main__":
    main()
