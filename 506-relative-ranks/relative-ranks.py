class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = {}
        l = score.copy()
        score.sort()
        k = []
        c = 1 
        for  i in range(len(score)-1,-1,-1):
            if c == 1 :
                d[score[i]] = "Gold Medal"
            elif c == 2:
                d[score[i]] = "Silver Medal"
            elif c == 3:
                d[score[i]] = "Bronze Medal"
            else:
                d[score[i]] = str(c)
            c += 1 
        for i in l:
            k.append(d[i])
        return k





        