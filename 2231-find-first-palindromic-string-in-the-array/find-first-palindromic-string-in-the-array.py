class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def palin(s):
            i = 0 
            j = len(s)-1
            while i<j:
                if s[i] != s[j]:
                    return 0 
                i += 1
                j -= 1
            return 1 
        for i in words:
            if palin(i) == 1:
                return i 
        return ""