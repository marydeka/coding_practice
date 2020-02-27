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
        '''
        1. create dict with original nodes and cloned nodes (with only val) as values
        2. create the next and random connections for cloned nodes by accessing dictionary
        '''
        
        clones = {}
        if not head:
            return None
        curr = head
        
        #create dict with original nodes as keys and clones as values
        while curr:
            clones[curr] = Node(curr.val)
            curr = curr.next
            
        #create next and random connections for clones
        for original, clone in clones.items():
            next_node = original.next
            random = original.random
            
            clone.next = None if next_node == None else clones[next_node]
            clone.random = None if random == None else clones[random]
            
        return clones[head]