# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#PREORDER

class Solution:
    def __init__(self):
        self.results = []
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        #root, left, right
        if root:
            self.results.append(root.val)
        else:
            return self.results
        
        if root.left:
            self.preorderTraversal(root.left)
        if root.right:
            self.preorderTraversal(root.right)
            
        return self.results

#POSTORDER

class Solution:
    def __init__(self):
        self.results = []
        
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        #left, right, root
        if not root:
            return self.results
        if root.left:
            self.postorderTraversal(root.left)
        if root.right:
            self.postorderTraversal(root.right)
        self.results.append(root.val)
        
        return self.results

#INORDER

class Solution:
    def __init__(self):
        self.results = []
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        #RECURSIVE SOLUTION
        #left, root, right
        if not root:
            return self.results
        if root.left:
            self.inorderTraversal(root.left)
        self.results.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)
            
        return self.results

        #ITERATIVE SOLUTION
