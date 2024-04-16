class Solution(object):
    def firstUniqChar(self, s):
        char_count = {}  #  initializam un dictionar pentru a numara aparitiile fiecarui caracter

        #  numaram aparitiile fiecarui caracter
        for char in s:
            if char in char_count:
                char_count[char] +=1
            else:
                char_count[char] = 1

        #  cautam primul caracter unic si returnam indexul sau
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i

        #  daca nu exista returnam -1 ;)
        return -1

def main():
    solution = Solution()  #  se creeaza o instanta a clasei Solution()
    s = "leetcode"
    print(solution.firstUniqChar(s))  #  se apelezeaza medota shuffle() asupra instantei solution

main()