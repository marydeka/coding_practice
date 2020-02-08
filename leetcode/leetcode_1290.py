Leetcode 1290: Easy 
Category: Linked Lists, Base Conversion
Convert Binary Number in Linked List to Integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin_list = []
        #continue to append current node's value to a list
        if not head:
            return 0
        else:
            while head:
                bin_list.append(head.val)
                head = head.next

        #convert the binary number (stored as a list) into a decimal num
        dec_num = 0
        multiplier = 1
        for i in range (len(bin_list) - 1, -1, -1):
            # print(i)
            dec_num += bin_list[i] * multiplier
            # print(f"dec num: {dec_num}")
            multiplier *= 2
        return dec_num