class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1 or n >= len(s):
            return s
        l = [[] for i in range(n)]
        ind = 0 
        d = 0 
        for  i in s: 
            if ind == 0 :
                d = 0
                l[ind].append(i)
                ind += 1 
            elif ind == n-1:
                l[ind].append(i)
                ind -= 1
                d = 1 
            elif d == 0 :
                l[ind].append(i)
                ind += 1 
            else:
                l[ind].append(i)
                ind -= 1
        k = ""
        for i in l:
            p = "".join(i)
            k += p 
        return k