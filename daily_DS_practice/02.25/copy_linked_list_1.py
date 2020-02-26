"""
Leetcode 138: Copy List with Random Pointer (medium)
https://leetcode.com/problems/copy-list-with-random-pointer/submissions/

Iteration 1
"""


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
        
        
        clones = {}
        
        if not head:
            return None
        
        current = head
        
        while current:
            clones[current] = Node(current.val)
            current = current.next
            
        for original, clone in clones.items():
            next_node = original.next
            random_node = original.random
            
            clone.next = None if next_node == None else clones[next_node]
            clone.random = None if random_node == None else clones[random_node]
            
        return clones[head]
        