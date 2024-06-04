class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = 0 
        d = {}
        for i in s:
            if  i not in d:
                d[i] = 1
            else:
                d[i] += 1
        a = True 
        for  i,j in d.items():
            if  j%2 == 0 :
                cnt += j 
            else :
                a = False
                cnt += j-1
        if a == False:
            cnt += 1 
        return cnt