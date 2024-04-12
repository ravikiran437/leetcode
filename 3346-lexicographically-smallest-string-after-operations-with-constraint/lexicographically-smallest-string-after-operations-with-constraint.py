class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        p = ""
        for i in s:
            a = ord(i)-96
            b = a-ord("a")+96
            c = 26 - a+1
            m = min(b,c)
            # print(m)
            if i == "a":
                p += i 
            elif k>=m:
                p += "a"
                k -= m
            else:
                if k!=0:
                    a = ord(i)-k
                    p += chr(a)
                    k = 0 
                else:
                    p += i
        return p 
        