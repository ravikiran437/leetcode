class Solution:
    def countDays(self, d: int, m: List[List[int]]) -> int:
        m.sort()
        c = 0 
        pre = m[0][1]
        c += (m[0][0]-1)
        for i,j in m[1:] :
            if i > pre:
                c += (i-pre-1)
                pre = j 
            if pre < j :
                pre = j 
        e = d - pre 
        if e > 0:
            c += (d-pre)
        return c