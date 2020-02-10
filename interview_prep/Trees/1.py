"""
Implement Binary Search Tree (BST)
"""

#create a class to create a node, with properties: left, right, count, and key

class Node:

    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None

#function to do inorder traversal of tree to find a key
def inorder(root): 
    if root != None: 
        inorder(root.left) 
        print(root.key)  
        inorder(root.right) 
  
#function to insert a new node.  
def insert(node, key): 
      
    # If tree is empty, create a new node  
    if node == None: 
        new_node = Node(key) 
        return new_node 
  
    # If key already exists in BST, do nothing (other option is to increment count variable)  
    if key == node.key: 
        return node 
  
    # Otherwise, use recursion to go down the tree  
    if key < node.key:  
        node.left = insert(node.left, key)  
    else: 
        node.right = insert(node.right, key) 
  
    # return node pointer  
    return node 

#function to delete a node

#function to find node with min val
def minValueNode(node): 
    current = node  
  
    # loop down to find the leftmost leaf  
    while current.left != None:  
        current = current.left  
  
    return current 

#function to find node with max val
def maxValueNode(node):
    current = node

    while current.right != None:
        current = current.right

    return current

root = None
root = insert(root, 12)  
root = insert(root, 10)  
root = insert(root, 20)  
root = insert(root, 9)  
root = insert(root, 11)  

print("Inorder traversal of tree")  
inorder(root)  

  



