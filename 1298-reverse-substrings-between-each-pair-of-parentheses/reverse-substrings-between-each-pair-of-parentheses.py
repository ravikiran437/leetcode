class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [["",""]]
        p = ""
        for i in s:
            if i == "(" :
                stack.append([i,""])
            elif stack and i!=")" :
                stack[-1][-1] += i 
            elif i == ")":
                p = stack[-1][-1] 
                p = p[::-1]
                stack.pop()
                stack[-1][-1] += p
        return stack[-1][-1]
        