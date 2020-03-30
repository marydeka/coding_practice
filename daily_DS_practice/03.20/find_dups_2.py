'''
Iteration 2:
Time: 15 min
Problem: return duplicates in an array
'''

# arr = [1,2,3]
arr = [2,1,2,2,1]

seen = set()
dups =[]

for num in arr:
    if num not in seen:
        seen.add(num)
    elif num not in dups:
        dups.append(num)

print(dups)