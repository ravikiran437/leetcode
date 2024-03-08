# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s,t = "",""
        while l1:
            s += str(l1.val) 
            l1 = l1.next 
        while l2:
            t += str(l2.val) 
            l2 = l2.next 
        s,t = s[::-1],t[::-1]
        a = int(s) + int(t)
        l = list(str(a))
        l = list(map(int,l))
        l = l[::-1]
        k = ListNode(l[0])
        tt = k
        for i in l[1:]:
            nn =   ListNode(i)
            tt.next = nn 
            tt = nn 
        return k    
        