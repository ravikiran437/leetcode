class Solution:
    def longestSubarray(self, l: List[int]) -> int:
        m = 1
        n = len(l)
        a = []
        zeros = [i for i in range(len(l)) if l[i]==0]
        if len(zeros) == 0 or len(zeros) == 1 :
            return n-1
        for i in range(len(zeros)-m+1):
            back = i-1
            front = i + m 
            if back < 0:
                back = 0
                a.append(zeros[front]-0)
    
            elif front >=len(zeros):
                front = n
                a.append(front-zeros[back]-1)
            else:
                a.append(zeros[front]-zeros[back]-1)
        return max(a)-1