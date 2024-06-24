# Time Complexity: O(N)
class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = []
        rest = []
        min_len = min(len(word1), len(word2))
      
        for i in range(min_len): # adding content of word1/word2 when they're same dimensions 
            res.append(word1[i]) 
            res.append(word2[i])  
          
        if len(word1) > len(word2): # adding the rest of word1 (if there is some) to the rest list
            rest.append(word1[min_len:])
        elif len(word1) < len(word2): # adding the rest of word2 (if there is some) to the rest list
            rest.append(word2[min_len:])
        
        return "".join(res+rest) # joining res with rest


def main() -> None:
    sol = Solution()
    word1 = "abc"
    word2 = "pqr"
    print(sol.mergeAlternately(word1, word2))

if __name__ == "__main__":
    main()
