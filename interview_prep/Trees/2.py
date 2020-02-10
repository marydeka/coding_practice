#function to delete a node
def deleteNode(root, key): 
      
    if root == None: 
        return root 
  
    # If the key to be deleted is smaller than the  
    # root's key, then it's in the left subtree  
    if key < root.key: 
        root.left = deleteNode(root.left, key)  
  
    # If the key to be deleted is greater than  
    # the root's key, then it lies in right subtree  
    elif key > root.key:  
        root.right = deleteNode(root.right, key)  
  
    # if key is same as root's key, and there's no child or just 1 child
    else: 
        if root.left == None: 
            temp = root.right 
            return temp 
        elif root.right == None: 
            temp = root.left 
            return temp 
  
        # node with two children: Get the inorder  
        # successor (smallest in the right subtree)  
        temp = minValueNode(root.right)

        # Copy the inorder successor's content 
        # to this node  
        root.key = temp.key  
  
        # Delete the inorder successor  
        root.right = deleteNode(root.right, temp.key) 
    return root 