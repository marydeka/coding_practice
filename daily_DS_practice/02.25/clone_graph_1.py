
'''
Leetcode 133: Clone Graph (medium)
https://leetcode.com/problems/clone-graph/

1st iteration
'''

from collections import deque
import pprint

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
        1. add each original clone to a dictionary and set value as a clone of that with no neighbors
        2. go through graph again give clones 
        
        '''
        
        clones = {}
        visited = []
        
        q = deque()
        
        if node:
            q.append(node)
        elif node == None:
            # print("entered")
            return None     #returning [] doesn't work
        
        while q:
            current = q.popleft()
            clones[current] = Node(current.val, [])
            visited.append(current)
            
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    q.append(neighbor)
          
        # pp = pprint.PrettyPrinter(indent = 4) 
        # pp.pprint(clones)
        
        for original, clone in clones.items():
            for neighbor in original.neighbors:
                clone.neighbors.append(clones[neighbor])
                
        # pp = pprint.PrettyPrinter(indent = 4) 
        # pp.pprint(clones)
        
        # for clone in clones.keys():
        #     print(clone.val)
        #     print(clones[clone].neighbors)
        
        return clones[node]
        
        