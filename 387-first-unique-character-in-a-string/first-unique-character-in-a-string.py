class Solution:
    def firstUniqChar(self, s: str) -> int:
        c=-1
        for i in range(len(s)):
            if s.count(s[i])==1:
                return i
        return c