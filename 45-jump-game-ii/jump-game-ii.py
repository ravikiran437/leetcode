class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [nums[0]]
        n = len(nums)
        if n == 1:
            return 0
        m = 0 
        for i in range(1,n):
            if i <= dp[-1]:
                m = max(m,nums[i]+i)
            else:
                dp.append(m)
                m = max(m,nums[i]+i)
        return len(dp)

        

        