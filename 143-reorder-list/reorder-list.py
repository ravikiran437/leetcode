# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = []
        t = head
        while head:
            l.append(head.val)
            head = head.next 
        k = []
        i = 0 
        j  = len(l)-1 
        while i<j:
            k.append(l[i])
            k.append(l[j])
            i += 1 
            j -= 1 
        if len(l)%2 == 1:
            k.append(l[len(l)//2])
        p = 0 
        while t:
            t.val = k[p]
            t = t.next 
            p += 1 
        return t