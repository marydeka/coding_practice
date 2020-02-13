#Implementation 1 of K-Way Merge

import heapq
from collections import deque

list1 = [2, 5, 10, 14, 19, 32]
list2 = [3, 5, 8, 16, 23, 28]
list3 = [1, 6, 17, 21, 29, 35]

# merged_list = list(merge(list1, list2, list3))
# print(merged_list)



#Implementation 2 of K-Way Merge

all_lists = [list1, list2, list3]

all_lists = [deque(a_list) for a_list in all_lists]
priority_q = []

#first step: take smallest item (leftmost) from each sorted list 
#and store in min priority queue

#find max length of all the lists so we know how many times to iterate
max_length = max(len(list1), len(list2), len(list3))

#after the while loop, our priority queue(stored in min_heap) should be complete
while max_length > 0:
    for a_list in all_lists:
        #can only pop from a list that isn't empty
        if len(a_list) > 0:
            heapq.heappush(priority_q, a_list.popleft())
    max_length -= 1

merged_list = []

# print(priority_q)

#now, while priority queue isn't empty
#pop from the priority_queue (min heap, so smallest item will be popped first)
#and append each item to merged_list

while priority_q:
    merged_list.append(heapq.heappop(priority_q))
    # print(merged_list)

print(merged_list)



