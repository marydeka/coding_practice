# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        list_merged = current = ListNode(0)
        
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    current.next = ListNode(l1.val)
                    current = current.next
                    l1 = l1.next
                else:
                    current.next = ListNode(l2.val)
                    current = current.next
                    l2 = l2.next
            else:
                if not l1:
                    current.next = ListNode(l2.val)
                    current = current.next
                    l2 = l2.next
                else:
                    current.next = ListNode(l1.val)
                    current = current.next
                    l1 = l1.next
            
        return list_merged.nex