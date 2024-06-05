class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        l = []
        for i in words:
            k = [0] * 26 
            for j in i :
                k[ord(j)-97] += 1 
            l.append(k)
        p = l[0]
        for i in l[1:]:
            for j in range(len(i)):
                p[j] = min(p[j],i[j])
        a = []
        for i in range(26):
            if p[i] != 0:
                b = [chr(i+97)]*p[i]
                a += b 
        return a


        