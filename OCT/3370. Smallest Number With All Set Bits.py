class Solution(object):
    def smallestNumber(self, n):
        """
        1: 1        - 2^0 - 1
        3: 11       - 2^1 - 1
        7: 111      - 2^2 - 1
        15: 1111    - 2^3 - 1
        31: 11111   - 2^4 - 1
        63: 111111  - 2^5 - 1
        """
        msb = n.bit_length() - 1
        return (1 << (msb + 1)) - 1
             
def main():
    solution = Solution()
    n = 5
    result = solution.smallestNumber(n)
    print(result)
        
if __name__ == "__main__":
    main()
