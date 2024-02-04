class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower()
        t = text.split()
        d = {}
        for i in t:
            l  = len(i)
            if l not in d:
                d[l] = []
                d[l].append(i)
            else:
                d[l].append(i)
        k = []
        for i ,j in d.items():
            k.append([i,j])
        k.sort()
        s = []
        for i, j in k:
            s.extend(j)
        s = " ".join(s).capitalize()
        return s
        
        