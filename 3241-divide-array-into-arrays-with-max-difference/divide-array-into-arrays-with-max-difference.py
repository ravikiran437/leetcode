class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        c =0 
        p = []
        for j in range(0,len(nums)-1,3):
            kk = nums[j:j+3]
            for i in range(len(kk)-2):
                if abs(kk[i]-kk[i+1])<=k and abs(kk[i+1]-kk[i+2])<=k and abs(kk[i]-kk[i+2])<=k:
                    c = c+1
                    p.append(kk)
        l = len(nums)//3 
        if c!=l:
            return []
        return p
        
        