'''
Leetcode problems 144, 94, and 145 (medium)

Iteration 1
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = []
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        '''
        1. Preorder: node, left, right
        '''
        
        if not root:
            return []
        
        self.result.append(root.val)
        if root.left:
            self.preorderTraversal(root.left)
        if root.right:
            self.preorderTraversal(root.right)
            
        return self.result
        
            

class Solution:
    def __init__(self):
        self.result = []
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        #printing nodes
        
        # if root.left:
        #     self.inorderTraversal(root.left)
        # print(root.val)
        # if root.right:
        #     self.inorderTraversal(root.right)
        
        result = []
        
        if root.left:
            self.inorderTraversal(root.left)
        self.result.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)
            
        return self.result

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.result = []
        
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return self.result
        
        if root.left:
            self.postorderTraversal(root.left)
        if root.right:
            self.postorderTraversal(root.right)
        self.result.append(root.val)
        
        return self.result