class Solution(object):
    def longestPalindrome(self, s):
        hashtable = {} # empty dict
        there_is_a_one = False
        counter = 0
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        else: 
            # create hashmap
            for elem in s:
                if elem in hashtable:
                    hashtable[elem] += 1
                else:
                    hashtable[elem] = 1
            # print(hashtable)
            # iterate over each value of hashmap
            for value in hashtable.values():
                while value > 1 and value % 2 == 1:
                    counter += 2
                    value -= 2
                if value > 1:
                    counter += value
                elif value == 1:
                    there_is_a_one = True
            if there_is_a_one:
                counter+=1
            return counter





def main() -> None:
    sol = Solution()
    s = "bananas"
    print(sol.longestPalindrome(s))

if __name__ == "__main__":
    main()
