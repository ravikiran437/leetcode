class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        c = nums[0]
        m = -1
        for i in range(1,len(nums)):
            if nums[i] < c : 
                c += nums[i]
                m = max(c,m)
            else:
                c += nums[i]
        return m
        