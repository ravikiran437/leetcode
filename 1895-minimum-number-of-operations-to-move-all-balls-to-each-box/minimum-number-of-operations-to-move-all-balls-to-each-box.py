class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        d = []
        for i in range(len(boxes)):
            if boxes[i] == "1":
                d.append(i)
        l = []
        for i in range(len(boxes)):
            c = 0 
            for j in  d:
                c += abs(j-i)
            l.append(c)
        return l
        