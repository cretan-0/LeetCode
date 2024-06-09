class Solution(object):
    def maximumEnergy(self, energy, k):
        res = []
        i = 0
        while i < len(energy) and i + k <= len(energy):
            if energy[i] + energy[k] < energy[k]:
                a = energy[k]
            else:
                a = energy[i] + energy[k]
            i += 1
            k += 1
            res.append(a)
        return max(res)




def main() -> None:
    sol = Solution()
    energy = [-2,-3,-1]
    k = 2
    print(sol.maximumEnergy(energy, k)) # 3



if __name__ == "__main__":
    main()
