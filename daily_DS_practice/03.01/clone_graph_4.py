'''
Iteration 4
Time: 25 min
Link to problem: https://leetcode.com/problems/clone-graph/submissions/

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
        #store all original nodes in dictionary, with clones as values
        originals = {}
        #remember to keep track of all visited nodes
        visited = []
        
        #do bfs traversal to get all original nodes
        q = deque()
        
        if not node:
            return None
        
        q.append(node)
        
        while q:
            curr = q.popleft()
            originals[curr] = Node(curr.val)
            visited.append(curr)
            if curr.neighbors:
                for neighbor in curr.neighbors:
                    if neighbor not in visited:
                        q.append(neighbor)
                    
        #give clone nodes neighbors
        for original, clone in originals.items():
            if original.neighbors:
                for neighbor in original.neighbors:
                    clone_neighbor = originals[neighbor]
                    clone.neighbors.append(clone_neighbor)
                    
        return originals[node]
        
        