class Solution:
    def minSubArrayLen(self, t: int, nums: List[int]) -> int:
        c = 0 
        start = 0 
        m = float("inf")
        for i in range(len(nums)):
            c = c + nums[i] 
            d = 0
            while c > t and start <= i:
                c = c -  nums[start]
                start += 1
                d = 1
            if c == t:
                m = min(i-start+1,m)
            elif c <t and d == 1:
                m = min(i-start+2,m)
        if m == float("inf"):
            return  0 
        return m
                