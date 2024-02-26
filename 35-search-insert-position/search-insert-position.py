class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        c=0
        for i in range(len(nums)):
            if nums[i]>=target:
                c=i
                break
            else:
                c=len(nums)
        return c
