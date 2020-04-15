from collections import deque

"""
'''
Problem: clone graph
Iteration: 8
Time: 30 min
'''


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        originals = {}
        visited = []
        q = deque()
        
        if not node:
            return None
        q.append(node)
        
        # create dict with all original nodes, clones as values (without neighbors)
        while q:
            curr = q.popleft()
            visited.append(curr)
            # print(curr.val)
            originals[curr] = Node(curr.val)
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    q.append(neighbor)
                    
        #create clone neighbors
        for orig, clone in originals.items():
            if orig.neighbors:
                for neighbor in orig.neighbors:
                    neighbor_clone = originals[neighbor]
                    clone.neighbors.append(neighbor_clone)
                    
                    
        return originals[node]
                
        
        