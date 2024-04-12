class Solution:
    def maxArea(self, ht: List[int]) -> int:
        i = 0 
        j = len(ht)-1
        ma = float("-inf")
        while i<=j:
            m = min(ht[i],ht[j])
            p = m*(j-i)
            ma = max(p,ma)
            if ht[i] == m:
                i+=1
            else:
                j -= 1
        return ma
        