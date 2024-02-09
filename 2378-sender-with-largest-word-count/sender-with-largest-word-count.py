class Solution:
    def largestWordCount(self, ms: List[str], ss: List[str]) -> str:
        d = {}
        for i in range(len(ss)):
            sp = ms[i].split()
            if ss[i] not in d:
                d[ss[i]]  = len(sp)
            else:
                d[ss[i]] += len(sp)
        m = max(d.values())
        k = []
        for i,j in d.items():
            if j == m:
                k.append(i)
        k.sort()
        return k[-1]
                