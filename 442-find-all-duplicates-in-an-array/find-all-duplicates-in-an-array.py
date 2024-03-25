class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        k = []
        s = set()
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                k.append(i)
        return k
