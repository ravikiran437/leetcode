class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        for i in range(len(s)-1,0,-1):
            k = s[i:]
            k = k[::-1]
            p = k + s 
            if p == p[::-1] :
                return p
        return s
        