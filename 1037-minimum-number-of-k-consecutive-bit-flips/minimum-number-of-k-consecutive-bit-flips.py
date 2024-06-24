from collections import deque
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        q = deque()
        c = 0 
        d = 0 
        for i in range(len(nums)):
            if q and q[0] <i-k+1:
                q.popleft()
            if i >= len(nums)-k+1:
                if nums[i] == 1 and len(q) %2 == 1:
                    nums[i] = 0 
                elif nums[i] == 0 and len(q)%2 == 1:
                    nums[i] = 1
                    c += 1
                elif nums[i] == 1:
                    c += 1
            elif nums[i] == 0 and len(q)%2 == 0:
                nums[i] = 1
                q.append(i)
                d += 1
                c += 1
            elif nums[i] == 1 and len(q)%2 == 1:
                nums[i] = 1 
                q.append(i)
                c += 1
                d += 1
            elif nums[i] == 0 and len(q)%2 == 1:
                nums[i] = 1
                c += 1
            else:
                c += 1
        if c == len(nums):
            return d 
        return -1
                