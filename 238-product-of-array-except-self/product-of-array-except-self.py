
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        c = 0 
        for i in nums:
            if i == 0 :
                c += 1 
            else:
                pro *= i 
            if c == 2:
                break 
        if c == 2:
            return [0]*len(nums)
        if c == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = pro 
                else:
                    nums[i] = 0 
            return nums 
        for i in range(len(nums)):
            nums[i] = pro//nums[i]
        return nums

