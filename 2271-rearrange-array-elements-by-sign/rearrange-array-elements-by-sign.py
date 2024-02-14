class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p,n=[],[]
        for i in nums:
            if i>0:
                p.append(i)
            else:
                n.append(i)
        k = []
        for i in range(len(p)):
            k.append(p[i])
            k.append(n[i])
        return k

        