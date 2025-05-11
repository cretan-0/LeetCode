class Solution(object):
    def threeConsecutiveOdds(self, arr):
        three_consec = 0
        l = 0
        while l <= len(arr) - 1:
            if arr[l] % 2 == 1:
                three_consec +=1
                if three_consec == 3:
                    return True
            else:
                three_consec = 0
            l += 1

        return False
