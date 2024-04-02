
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def iso(s):
            d = {}
            c = 1
            p  = ""
            for i in s:
                if i not in d:
                    p += str(c)
                    d[i] = c 
                    c += 1 
                else:
                    p += str(d[i])
            return p
        if iso(s) == iso(t): return 1
