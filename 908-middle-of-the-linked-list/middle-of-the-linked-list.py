# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next 
        l  =l[len(l)//2:]
        ll = ListNode(l[0])
        t = ll
        for i in l[1:]:
            nn = ListNode(i)
            t.next = nn 
            t = nn
        return ll