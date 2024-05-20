# from itertools import combinations
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        k = 2 ** n 
        l = 0
        for i in range(1,k):
            a = []
            for j in range(32):
                if (i>>j)&1 == 1 :
                    a.append(nums[j])
            c = 0 
            for i in a:
                c ^= i 
            l += c 
        return l
            