
class Solution:
    def frequencySort(self, s: str) -> str:
        k=[]
        for i in set(s):
            k.append([s.count(i),i])
        k.sort(reverse=True)
        x=""
        for i,j in k:
            x+=(j)*i 
        return x
        
        
            