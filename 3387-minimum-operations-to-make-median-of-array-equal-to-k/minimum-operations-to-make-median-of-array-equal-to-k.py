class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        c = 0
        nums.sort()
        # print(nums)
        n  = len(nums)
        c += abs(nums[n//2]-k)
        nums[n//2] = k 
        # print(nums)
        for i in range(n//2):
            if nums[i]>k:
                c += abs(nums[i]-k)
                nums[i] = k 
        for i in range(n//2+1,n):
            if nums[i]<k:
                c += abs(nums[i]-k)
                nums[i] = k 
        # print(nums)
        return c
