# https://leetcode.com/problems/divide-array-into-equal-pairs/description/

class Solution(object):
    def lemonadeChange(self, bills):
        count = {5:0, 10: 0}
        for bill in bills:
            if bill == 5:
                count[5] += 1
            elif bill == 10:
                if count[5]:
                    count[5] -= 1
                    count[10] += 1
                else:
                    return False
            else:
                if count[5] and count[10]:
                    count[5] -= 1
                    count[10] -= 1
                elif count[5] >= 3:
                    count[5] -= 3
                else:
                    return False
        return True

def main() -> None:
    sol = Solution()
    bills = [5,5,5,10,20]
    print(sol.lemonadeChange(bills))

if __name__ == "__main__":
    main()

