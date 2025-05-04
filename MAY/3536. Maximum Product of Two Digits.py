# v1

import types
class Solution:
    def maxProduct(self, n: int) -> int:
        l = [int(elem) for elem in str(n)]
        l = sorted(l)
        return l[-1] * l[-2]

def main() -> None:
    n= 125
    print(Solution().maxProduct(n))

if __name__ == "__main__":
    main()


# v2

class Solution:
    def maxProduct(self, n: int) -> int:
        l = [int(elem) for elem in str(n)]
        z = []
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                a = l[i] * l[j]
                z.append(a)

        return max(z)



