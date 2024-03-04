class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i = 0 
        j = len(tokens)-1
        cnt = 0 
        m = 0 
        while i <= j :
            if tokens[i] <= power:
                cnt += 1 
                m = max(cnt,m) 
                power = power -tokens[i]
                i += 1 
            elif cnt >= 1 :
                power += tokens[j]
                cnt -=1  
                j -= 1
            else:
                return m 
        return m