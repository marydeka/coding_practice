# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#Preorder
class Solution:
    def __init__(self):
        self.results = []
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.results.append(root.val)
        if root.left:
            self.preorderTraversal(root.left)
        if root.right:
            self.preorderTraversal(root.right)
            
        return self.results

#Inorder
class Solution:
    def __init__(self):
        self.results = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        if root.left:
            self.inorderTraversal(root.left)
        self.results.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)
            
        return self.results

#Postorder
class Solution:
    def __init__(self):
        self.results = []
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        if root.left:
            self.postorderTraversal(root.left)
        if root.right:
            self.postorderTraversal(root.right)
        self.results.append(root.val)
        
        return self.results

