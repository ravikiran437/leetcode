class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        k=[]
        for i in strs:
            x="".join(sorted(i))
            k.append([x,i])
        d={}
        for i,j in k:
            if i not in d:
                d[i]=[]
                d[i].append(j)
            else:
                d[i].append(j)
        p=[]
        for j in d.values():
            p.append(j)
        return p
            
        




        
        



        
        