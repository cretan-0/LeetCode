class Solution(object):
    def differenceOfSums(self, n, m):
        div_by_m = 0
        not_div_by_m = 0
        for num in range(n+1):
            if num % m == 0:
                div_by_m += num
            else:
                not_div_by_m += num
        return (not_div_by_m - div_by_m)

def main():
    sol = Solution()
    n = 5
    m = 6
    print(sol.differenceOfSums(n, m))

if __name__ == "__main__":
    main()