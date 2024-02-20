class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d = {}
        temp = score.copy()
        score.sort(reverse=True)
        for i in range(len(score)):
            p = i+1
            if p == 1:
                d[score[i]] = "Gold Medal"
            elif p == 2:
                d[score[i]] = "Silver Medal"
            elif p == 3:
                d[score[i]] = "Bronze Medal"
            else:
                d[score[i]] = str(p)
        for i in range(len(temp)):
            temp[i] = d[temp[i]]
        return temp


        