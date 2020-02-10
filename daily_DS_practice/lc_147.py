'''
Leetcode 147: Insertion Sort List
Level: Medium
Category: Strings
Estimated Time Taken: 2 hrs
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return None
        if not head.next:
            return head
        
        head = head
        # current = prev.next
        
        #find length of linked list
        def get_length(head):
            count = 1
            while head.next:
                count += 1
                head = head.next
            return count
        
        length = get_length(head)
        print(length)
        
#         #iterate through all nodes, keeping track of minimum
        def find_smallest(current):
            head_node = current
            min_val = current.val
            smallest = current
            while current.next:
                current = current.next
                if current.val < min_val:
                    min_val = current.val
                    smallest = current
                    
            return smallest
        
        
        prev = find_smallest(head)
        print(prev)