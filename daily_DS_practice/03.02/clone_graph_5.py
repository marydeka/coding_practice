'''
Iteration 5
Time: 5 minutes
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
        if not node:
            return None
        
        originals = {}
        visited = []
        
        q = deque()
        q.append(node)
        while q:
            curr = q.popleft()
            originals[curr] = Node(curr.val)
            visited.append(curr)
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    q.append(neighbor)
                    
        for original, clone in originals.items():
            for neighbor in original.neighbors:
                clone_neighbor = originals[neighbor]
                clone.neighbors.append(clone_neighbor)
                
        return originals[node]
            