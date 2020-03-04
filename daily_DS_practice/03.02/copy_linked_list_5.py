'''
Iteration 5
Time: 7 min
Problem: https://leetcode.com/problems/copy-list-with-random-pointer/submissions/
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        originals = {}
        curr = head
        
        while curr:
            originals[curr] = Node(curr.val)
            curr = curr.next
            
        #create connections for clone nodes
        for original, clone in originals.items():
            original_next = original.next
            original_random = original.random
            
            clone.next = None if original_next == None else originals[original_next]
            clone.random = None if original_random == None else originals[original_random]
            
        return originals[head]