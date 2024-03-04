class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        k = []
        for i in nums:
            k.append([str(i)*10,i])
        k.sort(reverse = True)
        s = ""
        for  i,j in k:
            s += str(j)
        p = int(s)
        return str(p)

        
        