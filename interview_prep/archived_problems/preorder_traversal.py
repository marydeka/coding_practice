"""
Leetcode 589. Easy

Given an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Follow up:

Recursive solution is trivial, could you do it iteratively?

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

def preorder(root):
    """
    :type root: Node
    :rtype: List[int]
    """
    
    results = []
    queue = []
    
    if root == None:
        return results
    
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        results.append(node.val)
        stack = []
        for child in node.children:
            stack.append(child)
        
        while len(stack) > 0:
            queue.insert(0, stack.pop())
    
    return results

print(preorder([1,null,3,2,4,null,5,6]))