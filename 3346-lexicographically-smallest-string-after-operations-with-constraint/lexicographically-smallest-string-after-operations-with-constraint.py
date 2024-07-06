class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        string = ""
        for i in s:
            num = ord(i) - 96 
            a = num - 1 
            b = 27 - num 
            m = min(a,b)
            if m <= k :
                k -= m 
                string += "a"
            elif m > k :
                string += chr(num-k+96)
                k = 0 
            

        print(k)
        return string
        