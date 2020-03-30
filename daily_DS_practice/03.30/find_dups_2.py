'''
Problem: Find duplicates (byte by byte)
Time: 30 min
Iteration: 2
'''

arr = [1,3,3]
arr_dict = {}
dups = []

for num in range(1, len(arr) + 1):
    arr_dict[num] = 1

print(arr_dict)

for num in arr:
    if num in arr_dict and num not in dups:
        dups.append(num)

print(dups)
