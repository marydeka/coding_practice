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
        
        #create dict with original nodes as keys and clones as values (but without neighbors yet)
        clones = {}
        visited = []
        
        q = deque()
        q.append(node)
        
        while q:
            curr = q.popleft()
            if curr not in visited:
                clones[curr] = Node(curr.val)
                visited.append(curr)
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    q.append(neighbor)
                    
        #give clones neighbors
        for original, clone in clones.items():
            for neighbor in original.neighbors:
                neighbor_clone = clones[neighbor]
                clone.neighbors.append(neighbor_clone)
                
        return clones[node]
            