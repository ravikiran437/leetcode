class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1 
            else:
                d[i]+=1
        m=max(d.values())
        c=0
        for i in d.values():
            if i==m:
                c+=m 
        return c
            
        