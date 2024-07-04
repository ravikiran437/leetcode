class Solution:
    def minSubArrayLen(self, t: int, nums: List[int]) -> int:
        k= []
        c = 0 
        m = float("inf")
        for i in nums:
            c += i 
            k.append(i)
            if c >= t:
                while c > t:
                    c -= k.pop(0)
                if c == t:
                    m = min(m,len(k))
                elif c < t:
                    m = min(m,len(k)+1)
        if m == float("inf"):
            return 0 
        return m
                