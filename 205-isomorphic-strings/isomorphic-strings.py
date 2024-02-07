
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def iso(s):
            d = {}
            c = 1
            st = ""
            for i in s:
                if i not in d:
                    st += str(c)
                    d[i] = c
                    c += 1 
                else:
                    st += str(d[i])
            return st 
        if iso(s) == iso(t): return 1