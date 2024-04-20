class Solution(object):
    def restoreString(self, s, indices):
        res = [] # aici vom stoca rezultatul 
        hashmap = dict(zip(indices,s)) # se creeaza un dictionar in care indicii sunt keys pentru fiecare caracter din stringul s
        """
        4: "c", 5: "o", 6: "d", etc
        """
        sorted_hashmap = dict(sorted(hashmap.items())) # sortam elementele dictionarului in ordine crescatoare valorii keys
        for values in sorted_hashmap.values(): # iteram pt fiecare valoare in hashmap-ul deja sortat
            res += values   #  stocam valoarea de la key 0 in res, key 1 in res etc --> ['l', 'e', 'e', 't', 'c', 'o', 'd', 'e']
        return "".join(res) #  leetcode


def main():
    solution = Solution()
    s = "codeleet"
    indices = [4,5,6,7,0,2,1,3]
    print(solution.restoreString(s,indices))

main()