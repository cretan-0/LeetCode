from itertools import permutations

class Solution(object):
    def findEvenNumbers(self, digits):
        res = set()
        for perm in permutations(digits, 3):
            if perm[0] == 0:
                continue
            number = perm[0] * 100 + perm[1] * 10 + perm[2]
            if number % 2 == 0:
                res.add(number)
        return  sorted(res)


def main() -> None:
    digits = [1, 2, 3]
    print(Solution().findEvenNumbers(digits))

if __name__ == '__main__':
    main()
