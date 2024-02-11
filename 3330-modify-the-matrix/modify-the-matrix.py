class Solution:
    def modifiedMatrix(self, m: List[List[int]]) -> List[List[int]]:
        l = []
        for i in range(len(m[0])):
            p = []
            for j in range(len(m)):
                p.append(m[j][i])
            l.append(max(p))
        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == -1:
                    m[i][j] = l[j]
        return m