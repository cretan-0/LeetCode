class Solution(object):
    def arrayRankTransform(self, arr):
        sort_arr = sorted(arr)
        rankk = {}
        counter = 0
        ranklist = []
        for i in sort_arr:
            if i in rankk:
                rankk[i] = counter
            else:
                counter += 1
                rankk[i] = counter
        for i in arr:
            ranklist.append(rankk[i])
        return ranklist