class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = nums[:2]
        for i in nums[2:]:
            a = dp[-2] + i 
            b = -1 
            if len(dp) >= 3:
                b = dp[-3] + i 
            dp.append(max(a,b))
        return max(dp)

        
        