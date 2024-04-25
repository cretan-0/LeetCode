class Solution(object):
    def xorOperation(self, n, start):
        nums = [] # lista unde stocam fiecare element in parte
        result = 0 # initializare variabila pentru stocarea rezultatului
        for num in range(n): 
            nums.append(start + 2 * num) # adaugarea in lista nums a elementelor conform formulei
        for num in nums:  # iteram de-a lungul tuturor elementelor
            result ^= num # stocam in result rezultatul XOR-ului cu fiecare element in parte
        return result