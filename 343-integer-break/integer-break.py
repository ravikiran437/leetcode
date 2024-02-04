class Solution:
    def integerBreak(self, n: int) -> int:
        if n ==2 :
            return 1 
        if n == 3:
            return 2
        c = 1 
        while n>4:
            c = c*3 
            n = n -3 
        c = c*n
        return c
        