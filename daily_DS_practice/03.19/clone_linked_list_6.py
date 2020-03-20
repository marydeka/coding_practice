'''
Iteration 6:
Time: 13 min
Problem: clone linked list

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
        #create dictionary with original nodes as keys and clones(without pointers) as values
        if not head:
            return None
        
        originals = {}
        
        current = head
        
        while current:
            originals[current] = Node(current.val)
            current = current.next
            
        #make connections for clone nodes
        for original, clone in originals.items():
            next_orig = original.next
            random_orig = original.random
            clone.next = None if next_orig == None else originals[next_orig]
            clone.random = None if random_orig == None else originals[random_orig]
            
        return originals[head]