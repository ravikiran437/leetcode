class Solution:
    def trap(self, h: List[int]) -> int:
        a,b = h[0] ,h[-1]
        pre,suf = [a],[b]
        for i in range(1,len(h)):
            if h[i]>a:
                a = h[i]
            pre.append(a)
        for j in range(len(h)-2,-1,-1):
            if h[j] > b :
                b = h[j]
            suf.append(b)
        suf = suf[::-1]
        cnt = 0 
        for i in range(len(pre)):
            cnt += min(abs(suf[i]-h[i]),(abs(h[i]-pre[i])))
        return cnt
        