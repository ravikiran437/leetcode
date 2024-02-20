class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        x=[]
        for i in s:
            if x==[]:
                x.append(i)
            elif len(x)>=(k-1) and x[-(k-1):]==list(i*(k-1)) :
                for i in range(k-1):
                    x.pop()

            else:
                x.append(i)
        return "".join(x)
        