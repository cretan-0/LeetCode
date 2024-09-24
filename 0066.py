class Solution(object):
    def plusOne(self, digits):
        if digits[-1] < 9:
            digits[-1] = digits[-1] + 1;
        elif digits[-1] == 9:
            digits[-1] = 1;
            digits.append(0)
        return digits
           
# 93/111 testcases passed - > to be solved


# 24/09/24

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        int_digits = int(''.join(map(str, digits)))
        int_digits += 1
        #int_digits = int_digits.split()
        int_digits = str(int_digits)
        res = [number for number in int_digits]
        res = list(map(int, res))
        return res



def main() ->  None:
    sol = Solution()
    digits = [1,2,3]
    print(sol.plusOne(digits))


if __name__ == "__main__":
    main()
