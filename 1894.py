class Solution(object):
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk) 
        rem = k % total

        # in this way we will loop over chalk only once time
        # because re reminder of k % total

        for i in range(len(chalk)):
            rem -= chalk[i]
            if rem < 0:
                return i
        return -1
