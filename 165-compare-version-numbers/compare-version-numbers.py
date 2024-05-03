class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        s1 = v1.split(".")
        s2 = v2.split(".")
        p,q = [],[]
        a,b = "",""
        for i in s1:
            p.append(int(i))
            a += i 
        for i in s2:
            q.append(int(i)) 
            b += i 
        for i in range(len(min(p,q))):
            if p[i] > q[i]:
                return 1 
            elif p[i] < q[i]:
                return -1 
        def fun(s):
            k = ""
            for i in s:
                k += str(i)
            return int(k)
        if len(p) > len(q):
            p = p[len(q):]
            if fun(p) !=0 :
                return 1
        elif len(p) < len(q):
            q = q[len(p):]
            if fun(q) != 0 :
                return -1
        return 0