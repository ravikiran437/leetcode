class Solution:
    def compressedString(self, word: str) -> str:
        prev = word[0]
        k = []
        c = 1
        for i in word[1:]:
            if i == prev:
                c += 1 
            else:
                k.append([prev,c])
                c = 1
            prev = i
        k.append([prev,c])
        s = ""
        for i,j in k:
            if j <= 9:
                s += str(j) + i 
            else:
                mod = j % 9
                div = j // 9 
                p = ("9"+i)*div 
                s += p
                if mod != 0 :
                    s += str(mod)+i 
        return s



        