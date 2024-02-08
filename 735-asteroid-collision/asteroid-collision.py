class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        def stack(a):
            k = []
            for i in a:
                if len(k)>0:
                    if k[-1] > 0 and i < 0:
                        if abs(i) > k[-1] : 
                            k.pop()
                            k.append(i)
                        elif abs(i) == k[-1]:
                            k.pop()
                    else:
                        k.append(i)
                else:
                    k.append(i)
            if len(k) == len(a):
                return k 
            return stack(k)
        return stack(a)