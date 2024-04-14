class Solution(object):
    def plusOne(self, digits):
        if digits[-1] < 9:
            digits[-1] = digits[-1] + 1;
        elif digits[-1] == 9:
            digits[-1] = 1;
            digits.append(0)
        return digits
           
#93/111 testcases passed