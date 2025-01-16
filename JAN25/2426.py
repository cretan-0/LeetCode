class Solution(object):
    def xorAllNums(self, nums1, nums2):
        nums3 = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                a = nums1[i] ^ nums2[j]
                nums3.append(a)
        print(nums3)
        # pairs are good
        
        
        res = 0
        for i in range(len(nums3)-1):
            a = nums3[i] ^ nums3[i+1]
            res += a
        
        return res


        
def main() -> None:
    sol = Solution()
    nums1 = [2,1,3]
    nums2 = [10,2,5,0]
    print(sol.xorAllNums(nums1, nums2))
    
    
    
if __name__ == "__main__":
    main()
    
