# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next 
        l = l[::-1]
        if l:
            ll = ListNode(l[0])
            t = ll 
            for i in l[1:]:
                nn = ListNode(i)
                t.next = nn
                t = nn 
            return ll 
        return None

             
        