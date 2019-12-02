"""
Leetcode 590. Easy

Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Follow up:

Recursive solution is trivial, could you do it iteratively?

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]

"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

def postorder(self, root):
    """
    :type root: Node
    :rtype: List[int]
    """
    result = []
    
    if root == None:
        return result
    stack = [root]
    while stack:
        root = stack.pop()
        result.append(root.val)
        
        #extends adds every element in the iterable
        stack.extend(root.children) 
    return result[::-1]

print(postorder([1,null,3,2,4,null,5,6]))