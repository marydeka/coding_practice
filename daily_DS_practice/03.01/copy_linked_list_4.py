'''
Iteration 4
Time: 18 min
Link to Problem: https://leetcode.com/problems/copy-list-with-random-pointer/submissions/
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
        #put all original nodes into dictionary and store clones (without connections) as values
        originals = {}
        
        if not head:
            return None
        current = head
        
        while current:
            originals[current] = Node(current.val)
            current = current.next
            
        #create connections for clone nodes
        for original, clone in originals.items():
            if original.next == None:
                clone_next = None
            else:
                clone_next = originals[original.next]
            if original.random == None:
                clone_random = None
            else:
                clone_random = originals[original.random]
            clone.next = clone_next
            clone.random = clone_random
            
        return originals[head]