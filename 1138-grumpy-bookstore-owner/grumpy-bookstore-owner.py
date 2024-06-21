class Solution:
    def maxSatisfied(self, l1: List[int], l2: List[int], n: int) -> int:
        sum1 = 0 
        for i in range(len(l1)):
            if l2[i] == 0:
                sum1 += l1[i]
        a = l1[:n]
        b = l2[:n]
        c = 0 
        s = 0 
        for i in range(n):
            if l2[i] == 0 :
                c += a[i]
            s += l1[i]
        m = sum1-c+s
        for i in range(n,len(l1)):
            a.append(l1[i])
            b.append(l2[i])
            p = a.pop(0)
            q = b.pop(0)
            s -= p 
            s += l1[i]
            if q == 0:
                c -= p 
            if l2[i] == 0:
                c += l1[i] 
            m = max(m,s+sum1-c)
        return m
        