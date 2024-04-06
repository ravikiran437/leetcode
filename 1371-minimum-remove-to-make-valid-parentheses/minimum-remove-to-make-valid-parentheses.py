class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        k = []
        p = []
        c = 0
        cnt = 0
        for i in s:
            if i == '(':
                k.append([i,cnt])
            elif i == ")" and len(k)!=0:
                p.insert(k[0][1]-c,"(")
                p.append(")")
                k.pop(0)
            else:
                if i == ")":
                    c += 1
                if i!= ")":
                    p.append(i)
            cnt += 1
        return "".join(p)

        