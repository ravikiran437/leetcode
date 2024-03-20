# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l1,l2 = [],[]
        while list1:
            l1.append(list1.val)
            list1 = list1.next 
        while list2:
            l2.append(list2.val)
            list2 = list2.next 
        l11 = l1[:a]
        l12 = l1[b+1:]
        l11 = l11+l2+l12
        l = ListNode(l11[0])
        t = l
        for i in l11[1:]:
            nn = ListNode(i)
            t.next = nn 
            t = nn 
        return l
