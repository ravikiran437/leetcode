class Solution:
    def maxProfit(self, p: List[int]) -> int:
        k = p[-1]
        m = 0 
        for  i in range(len(p)-2,-1,-1):
            if k  < p[i]:
                k = p[i]
            else:
                m = max(m,k-p[i])
        return m



        return m

        
        