# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = 0
        temp = head
        while head:
            s = s * 10 + head.val
            head = head.next 
        s = s*2
        l = []
        while s:
            l.insert(0, s%10)
            s = s // 10
        
        if not l:
            return temp
        ll = ListNode(l[0])
        if len(l) == 1:
            return ll
        t = ll
        for i in l[1:]:
            nn = ListNode(i)
            t.next = nn
            t = t.next
        return ll
        

        
        