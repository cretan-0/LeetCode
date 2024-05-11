class Solution(object):
    def finalValueAfterOperations(self, operations):
        res = 0
        for op in operations:
            if op == "--X" or op == "X--":
                res -= 1
            else:
                res += 1
        return res

def main():
    sol = Solution()
    operations = ["--X","X++","X++"]
    print(sol.finalValueAfterOperations(operations))

if __name__ == "__main__":
    main()