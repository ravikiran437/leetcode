class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        c =  0
        for i in nums:
            if i not in s:
                nums[c] =  i 
                c += 1 
                s.add(i) 
        return c
        