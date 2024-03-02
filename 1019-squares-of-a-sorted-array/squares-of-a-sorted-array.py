class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def sq(n):
            return n**2 
        for i in range(len(nums)):
            nums[i] = sq(nums[i])
        nums.sort()
        return nums