class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one=s.count("1")
        if one==1:
            s="0"*s.count("0")+str(one)
            return s
        else:
            return "1"*(s.count("1")-1)+"0"*(s.count("0"))+"1"
        

        