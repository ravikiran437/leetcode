class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        arr = []
        k = []
        c = len(t)-1
        for i in t[::-1]:
            if k == []:
                k.append([i,c])
                arr.append(0)
            else:
                c = c-1
                while len(k)!= 0 :
                    if k[-1][0] <= i :
                        k.pop()
                    else:
                        arr.append(k[-1][1] - c)
                        k.append([i,c])
                        break
                else:
                    arr.append(0)
                    k.append([i,c])
        return arr[::-1]
        