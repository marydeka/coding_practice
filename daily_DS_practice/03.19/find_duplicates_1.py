'''
Iteration 1
Time: 20 min
Problem: Find duplicate in array

'''


arr1 = [3,3,3]

nums_seen = set()
dups = []

for i in range(1, len(arr1)):
    if arr1[i] in nums_seen:
        dups.append(arr1[i])
    else:
     nums_seen.add(arr1[i])
    

print(dups)