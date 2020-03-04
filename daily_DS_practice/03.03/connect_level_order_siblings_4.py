from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # level order traversal using 'next' pointer
  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val) + " ", end='')
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
        current = current.next
      print()


def connect_level_order_siblings(root):
  if not root:
    return None
  q = deque()
  q.append(root)

  while q:
    level_size = len(q)
    prev = None
    for node in range(level_size):
      curr = q.popleft()
      if prev:
        prev.next = curr
      prev = curr
      if curr.left:
        q.append(curr.left)
      if curr.right:
        q.append(curr.right)

  #Alternate Solution: keep track of current level
  if not root:
    return None
  q = deque()
  level = 0
  q.append([root, level])
  prev = None
  prev_level = None

  #first do bfs to give all nodes proper level
  while q:
    curr, curr_level = q.popleft()
    if prev:
      if prev_level == curr_level:
        prev.next = curr
    prev = curr
    prev_level = curr_level
    print("curr:" + str(curr.val) + ", curr_level:" + str(curr_level))
    # if len(q) == 0:
    #   level += 1
    if curr.left:
      q.append([curr.left, curr_level + 1])
    if curr.right:
      q.append([curr.right, curr_level + 1])


    

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_level_order_siblings(root)

  print("Level order traversal using 'next' pointer: ")
  root.print_level_order()


main()
