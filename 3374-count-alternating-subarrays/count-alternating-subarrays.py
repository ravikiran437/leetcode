class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        c = 1
        prev = nums[0]
        cnt = 0 
        for i in nums[1:]:
            if prev != i :
                c += 1 
            else:
                cnt += (c*(c+1))//2
                c  = 1
            prev = i
        cnt += (c*(c+1))//2 
        return cnt
            


        