class Solution:
    def pivotInteger(self, n: int) -> int:
        c=0
        for i in range(n,-1,-1):
            c=c+i
            if c==(i*(i+1))//2:
                return i
        return -1
      
        