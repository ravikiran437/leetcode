class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t = ""
        m = 0 
        for i in s:
            if i not in t:
                t += i 
            else:
                m = max(m,len(t))
                t = t[t.find(i)+1:]
                t= t+i
        m = max(m,len(t))
        return m
        