class Solution:
    def hIndex(self, cit: List[int]) -> int:
        cit.sort()
        n  = len(cit)
        for i in range(n):
            if cit[i] >= (n-i):
                return n-i
        return 0
