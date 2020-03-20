'''
Iteration 7:
Time: 16 min
Problem: Clone graph
'''


from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #create dict of original nodes as keys and clones without neighbors as values
        if not node:
            return None
        
        q = deque()
        q.append(node)
        
        originals = {}
        visited = []
        
        while q:
            curr = q.popleft()
            visited.append(curr)
            originals[curr] = Node(curr.val)
            if curr.neighbors:
                for neighbor in curr.neighbors:
                    if neighbor not in visited:
                        q.append(neighbor)
                        
        #create clone neighbors
        for original, clone in originals.items():
            for neighbor in original.neighbors:
                clone.neighbors.append(originals[neighbor])
                
        return originals[node]
            
                    
                    