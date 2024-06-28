class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        m = nums[0] 
        c = 0
        maxi = 0
        for i in nums[1:]:
            if m >i and maxi == 0 :
                m = i 
            else:
                if maxi > i :
                    c += maxi - m 
                    m = i 
                    maxi = 0 
                else:
                    maxi = i 
                # print(dp)
        #     print(dp,c,m)
        if maxi!=0:
            c += maxi - m
        return c
                