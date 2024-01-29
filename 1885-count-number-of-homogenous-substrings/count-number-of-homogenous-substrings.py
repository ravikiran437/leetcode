class Solution:
    def countHomogenous(self, s: str) -> int:
        c = 0
        x = 0
        m = (10**9)+7
        for  i in range(len(s)-1):
            if s[i] == s[i+1]:
                c += 1
            elif s[i]!= s[i+1]:
                c= c+1 
                x += ((c*(c+1))//2)%m
                c = 0 
        c += 1
        x += ((c*(c+1))//2)%m
        return x%m
        
        