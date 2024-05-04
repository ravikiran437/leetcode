class Solution:
    def numRescueBoats(self, p: List[int], l: int) -> int:
        cnt = 0 
        p.sort()
        i = 0 
        j = len(p)-1
        while i<=j:
            cnt += 1
            if p[i]+p[j] <= l :
                i += 1 
            j -= 1
        return cnt
        