from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        max = 0
        for elem1 in arr1:
            for elem2 in arr2:

                cp_arr1 = [int(digit) for digit in str(elem1)]
                cp_arr2 = [int(digit) for digit in str(elem2)]

                #print("outer loops", cp_arr1, cp_arr2)

                counter: int = 0
                for i in range(min(len(cp_arr1), len(cp_arr2))):
                    if cp_arr1[0] != cp_arr2[0]:
                        break
                    elif cp_arr1[i] != cp_arr2[i]:
                        break
                    elif cp_arr1[i] == cp_arr2[i]:
                        counter += 1

                    if counter > max:
                        max = counter
                   # counter = 0

        return max

def main() -> None:
    sol = Solution()
    arr1 = [1124,9304,8119]
    arr2 = [7782,3372,9864]
    print(sol.longestCommonPrefix(arr1, arr2))

if __name__ == '__main__':
    main()
