class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        k = [0] * n 
        stack = []
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            elif stack != [] and s[i] == ")":
                k[stack[-1]] = 1 
                k[i] = 1 
                stack.pop()
        cnt,maxi = 0,0 
        for i in k:
            if i == 1:
                cnt += 1 
            else:
                maxi = max(cnt,maxi)
                cnt = 0 
        maxi = max(maxi,cnt)
        return maxi
        
                
        