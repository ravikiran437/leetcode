import bisect
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(len(nums)+1):
            if i == n - bisect.bisect_left(nums,i):
                return i 
        return -1        

        