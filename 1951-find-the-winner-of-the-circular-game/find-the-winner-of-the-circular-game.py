class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = []
        c= 1
        for i in range(1,n+1):
            l.append(i)
        cnt = 0
        ind = 0
        while len(l)!=1:
            if c == k:
                l.pop(ind)
                c = 0
                cnt += 1
            else:
                ind += 1
            c = c + 1
            if ind == n-cnt:
                ind = 0
        return l[0]