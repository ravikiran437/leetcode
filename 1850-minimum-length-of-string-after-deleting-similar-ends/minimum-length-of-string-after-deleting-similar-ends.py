class Solution:
    def minimumLength(self, s: str) -> int:
        if len(set(s)) == 1 and len(s) == 1:
            return 1
        if len(set(s)) == 1 and len(s) >1:
            return 0
        i = 0
        j = len(s)-1
        while i<j:
            if s[i]!=s[j]:
                break
            if s[i] == s[j]:
                c = s[i]
                while s[i]==c:
                    i += 1 
                while s[j]==c:
                    j -= 1
        if i<=j:
            return j-i+1 
        return 0

        