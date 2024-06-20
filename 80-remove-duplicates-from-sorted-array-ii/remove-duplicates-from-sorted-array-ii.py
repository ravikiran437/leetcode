class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums = [0,0,1,1,1,1,2,3,3]
        prev = nums[0]
        c = 1
        d = 0
        for i in nums[1:]:
            if prev == i and d == 0:
                nums[c] = i 
                d = 1 
                c += 1 
            if prev != i:
                nums[c] = i 
                c += 1 
                d = 0 
            prev = i 
        return c


                