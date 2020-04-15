'''
Problem: merge k arrays
Iteration: 1
Time: 10 min
'''

import heapq

arrays = [[1,4,7],[2,5,8],[3,6,9]]
min_heap = []
final_list = []

for arr in arrays:
    for num in arr:
        heapq.heappush(min_heap, num)

while min_heap:
    smallest = heapq.heappop(min_heap)
    final_list.append(smallest)

print(final_list)