class Solution:
    def averageWaitingTime(self, c: List[List[int]]) -> float:
        t = 0
        avg = 0
        for i,j in c:
            if t < i :
                t = i 
            t +=  j 
            avg += (t-i)
        return avg/(len(c))