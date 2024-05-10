class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], kk: int) -> List[int]:
        k = []
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                k.append([arr[i]/arr[j],[arr[i],arr[j]]])
        k.sort()
        return k[kk-1][-1]
        