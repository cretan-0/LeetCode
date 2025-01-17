class Solution(object):
    def doesValidArrayExist(self, derived):
        return sum(derived)%2 == 0

def main() -> None:
  sol = Solution()
  derived = [1,1,0]
  print(sol.doesValidArrayExist(derived))

if __name__ == "__main__":
  main()
