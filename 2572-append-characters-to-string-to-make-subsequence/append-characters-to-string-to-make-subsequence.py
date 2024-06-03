class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        a = 0
        b = 0
        while a < len(s) and b < len(t):
            if s[a] != t[b]:
                a += 1
            else:
                a += 1
                b += 1
        return len(t)-b