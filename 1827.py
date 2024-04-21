class Solution(object):
    def findSpecialInteger(self, arr):
        arr2 = {}  # se creeaza un dictionar unde se vor stoca keys and values
        for i in arr:
            if i in arr2:
                arr2[i]+=1
            else:
                arr2[i] = 1
        keyVal = list(arr2.keys()) # lista cu keys
        val = list(arr2.values()) # lista cu values
        maxVal = max(val)  # se stabileste val max din lista val
        index = val.index(maxVal) # se stabileste index-ul valorii maxime
        return keyVal[index] # se returneaza din lista keyVal, index-ul val maxime