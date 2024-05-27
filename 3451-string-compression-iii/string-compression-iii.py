class Solution:
    def compressedString(self, word: str) -> str:
        prev = word[0]
        count = 1
        ans = ''
        for i in word[1:]:
            if prev == i and count < 9:
                count += 1
            else:
                ans += str(count) + prev
                prev = i
                count = 1
        ans += str(count) + prev
        return ans