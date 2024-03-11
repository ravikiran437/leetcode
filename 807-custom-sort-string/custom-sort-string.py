class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1 
            else:
                d[i] += 1
        x = "" 
        for i in order:
            if i in d:
                x +=  i* d[i]
                del d[i]
        if d:
            for i,j in d.items():
                x += i*j 
        return x

    
       