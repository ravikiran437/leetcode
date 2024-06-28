class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        m = nums[0] 
        c = 0
        dp = []
        for i in nums[1:]:
            if m >i and dp == [] :
                m = i 
            else:
                if dp and dp[-1] > i :
                    c += dp[-1]-m 
                    m = i 
                    dp = []
                else:
                    dp.append(i)
                # print(dp)
        #     print(dp,c,m)
        if dp:
            c += dp[-1] - m
        return c
                