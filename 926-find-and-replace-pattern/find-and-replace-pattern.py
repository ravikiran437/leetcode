class Solution:
    def findAndReplacePattern(self, words: List[str], s: str) -> List[str]:
        def word(s):
            d = {}
            c = 0
            p = ""
            for i in s:
                if i not in d:
                    c += 10
                    d[i] = c 
                    p += str(c)
                else:
                    p += str(d[i])
            return p
        w = word(s)
        k = []
        for i in range(len(words)):
            if word(words[i]) == w:
                k.append(words[i])
        return k
        
        