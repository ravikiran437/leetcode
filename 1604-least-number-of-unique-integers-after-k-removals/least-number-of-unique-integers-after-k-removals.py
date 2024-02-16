class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], s: int) -> int:
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1 
            else:
                d[i] += 1 
        k = []
        for i,j in d.items():
            k.append([j,i])
        k.sort()
        for i,j in k:
            if i<=s:
                del d[j]
                s = s - i
        return len(d)