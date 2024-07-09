class Solution:
    def averageWaitingTime(self, c: List[List[int]]) -> float:
        cnt = c[0][0] + c[0][1]
        total = cnt - c[0][0]
        for i,j in c[1:]:
            if i > cnt:
                cnt = i 
            cnt += j
            total += cnt - i 
        # print(total)
        return total/len(c)
