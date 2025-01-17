class Solution(object):
    def xorAllNums(self, nums1, nums2):
        res = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                res ^= nums1[i] ^ nums2[j]
        return res


        
def main() -> None:
    sol = Solution()
    nums1 = [2,1,3]
    nums2 = [10,2,5,0]
    print(sol.xorAllNums(nums1, nums2))
    
    
    
if __name__ == "__main__":
    main()
    
