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
        #create dict of original nodes and clones as values (without next and random pointers)
        
        if not head:
            return None
        
        clones = {}
        
        curr = head
        
        while curr:
            clones[curr] = Node(curr.val)
            curr = curr.next
            
        #create the pointers for the nodes
        for original, clone in clones.items():
            next_node = original.next
            random = original.random
            clone.next = None if next_node == None else clones[next_node]
            clone.random = None if random == None else clones[random]
            
        return clones[head]