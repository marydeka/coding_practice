def delete_nodes(head, key):
    if not head:
        return None

    prev = head
    if prev.val == key:
        while.prev.val == key and prev:
            prev = prev.next
    if prev == None:
        return None

    if prev.next = None:
        return prev

    head = prev.next

    while head:
        if head.val == key:
            while head.val == key and head:
                head = head.next
            prev.next = head
        head = head.next



'''
Working on Code:


def removeNodes(head, key):
  if not head:
    return None

  head_node = head
  if head_node.val == key:
    print("head node equals key")
    while head_node.val == key and head_node:
      print(head_node.next.val)
      head_node = head_node.next
  if head_node == None:
    return None

  if head_node.next == None:
    return head_node

  current = head_node.next
  prev = head_node

  while current:
    if current.val == key:
      while current and current.val == key:
        print(current.next.val)
        current = current.next
      print(prev.next.val)
      prev.next = current
    current = current.next
    prev = prev.next
    
    
  return head_node



'''