class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        h.sort()
        c = 0 
        x = 0 
        for i in range(len(h)-1,len(h)-k-1,-1):
            h[i] = h[i]-c 
            if h[i] < 0 :
                h[i] = 0 
            x += h[i]
            c += 1
        return x
