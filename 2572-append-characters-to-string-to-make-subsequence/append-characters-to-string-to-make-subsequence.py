class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l = list(t)
        c  = 0 
        for i in s:
            if l :
                if i == l[0]:
                    c += 1
                    l.pop(0)
        return len(t) - c


        