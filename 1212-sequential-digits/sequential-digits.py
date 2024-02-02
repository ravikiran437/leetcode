class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def digit(k,low,high,l):  
            s = ""
            for i in range(1,10):
                s  += str(i)
                p = int(s)
                if len(s) == k:
                    if p>=low and p<=high:
                        l.append(p)
                    s = s[1:]
            return 
        l = []
        for k in range(len(str(low)),len(str(high))+1):
            digit(k,low,high,l)
        return l
        