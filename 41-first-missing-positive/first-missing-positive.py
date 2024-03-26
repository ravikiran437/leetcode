class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        c = 0 
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] == 1 and c == 0:
                c = 1 
                pre = 1
            elif c == 1 and pre == nums[i]:
                pass 
            elif c == 1 and nums[i]!=pre+1:
                return pre+1
            else:
                pre = nums[i]
        if c == 0:
            return 1 
        if pre == nums[-1]:
            return pre+1
            
        
