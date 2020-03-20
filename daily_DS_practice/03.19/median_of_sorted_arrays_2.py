from heapq import heappush

arr1 = [1,3,5]
arr2 = [2,4,6]

min_heap = []
max_heap = []

for num in arr1:
    if len(min_heap) < len(max_heap):
        min_heap.heappush(num)
    elif len(max_heap) < len(min_heap):
        max_heap.heappush(num)
    