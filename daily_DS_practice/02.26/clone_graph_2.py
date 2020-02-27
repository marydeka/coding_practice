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
        '''
        1. use dfs or bfs to iterate through all nodes
        2. store original nodes in dictionary
        3. make sure no original nodes are stored twice (keep a visited list)
        4. store a cloned node as value to go with each original node 
        5. the cloned node will only be given a val
        6. to set the cloned node's neighbors, 
        '''
        
        clones = {}
        visited = []
        
        q = deque()
        if not node:
            return None
        q.append(node)
        
        #create dictionary of originals with clones as values
        while q:
            curr = q.popleft()
            visited.append(curr)
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    q.append(neighbor)
            clones[curr] = Node(curr.val)
            
        #connect clones to their neighbors
        for original, clone in clones.items():
            for neighbor in original.neighbors:
                cloned_neighbor = clones[neighbor]
                clone.neighbors.append(cloned_neighbor)
                
        return clones[node]
        