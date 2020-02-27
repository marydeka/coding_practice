from __future__ import print_function
from collections import deque


# class TreeNode:
#   def __init__(self, val):
#     self.val = val
#     self.left, self.right, self.next = None, None, None

#   # level order traversal using 'next' pointer
#   def print_level_order(self):
#     nextLevelRoot = self
#     while nextLevelRoot:
#       current = nextLevelRoot
#       nextLevelRoot = None
#       while current:
#         print(str(current.val) + " ", end='')
#         if not nextLevelRoot:
#           if current.left:
#             nextLevelRoot = current.left
#           elif current.right:
#             nextLevelRoot = current.right
#         current = current.next
#       print()


def connect_level_order_siblings(root):
  q = deque()
  if root:
    q.append(root)
  else:
    return
  #make all the linked list connections
  while q:
    level_size = len(q)
    prev = None
    for i in range(level_size):
      current = q.popleft()
      if prev:
        prev.next = current
      prev = current
    #add children of current node to queue
      if current.left:
        q.append(current.left)
      if current.right:
        q.append(current.right)
    

# def main():
#   root = TreeNode(12)
#   root.left = TreeNode(7)
#   root.right = TreeNode(1)
#   root.left.left = TreeNode(9)
#   root.right.left = TreeNode(10)
#   root.right.right = TreeNode(5)
#   connect_level_order_siblings(root)

#   print("Level order traversal using 'next' pointer: ")
#   root.print_level_order()


# main()




#the following code was an original attempt

def connect_level_order_siblings(root):
  level = 0
  q = deque()
  if root:
    q.append([root, level])
  else:
    return 

  while q:
    prev_node = None 
    cur_node, depth = q.popleft()
    #determine num of nodes on each level
    if not q:
      cur_node.next = None
    
    result.append(cur_node)
    if lev > level:
      level += 1
    if cur_node.left:
      q.append([cur_node.left, level])
    if cur_node.right:
      q.append([cur_node.right, level])