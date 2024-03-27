class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cnt = 1 
        n = len(nums)
        for i in nums:
            cnt *= i 
        if cnt < k:
            return ((n*(n+1))//2)
        c = 0
        d = 0
        for i in range(len(nums)):
            p  = nums[i]
            if p < k:
                d += 1
                a = [nums[i]]
                for j in range(i+1,len(nums)):
                    p *= nums[j]
                    if p<k:
                        d += 1
                    if p >= k :
                        break 
                c += d
                d = 0 
        return c
        