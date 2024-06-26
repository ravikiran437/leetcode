class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0 
        for i in range(len(nums)):
            if m < i :
                return 0
            ind = nums[i] + i 
            m = max(ind,m)
            
        return 1
            
