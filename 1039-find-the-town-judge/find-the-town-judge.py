class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if trust == [] and n == 1:
            return 1
        d = {}
        s = set()
        for i,j in trust:
            s.add(i)
            if j not in d:
                d[j] = 1
            else:
                d[j] += 1
        if d:
            for i,j in d.items():
                if j == n-1 and i not in s:
                    return i
        return -1