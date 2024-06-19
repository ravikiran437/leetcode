class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        c = 0 
        for i in range(m,len(nums1)):
            nums1[i] = nums2[c]
            c += 1
        nums1.sort()
      
        