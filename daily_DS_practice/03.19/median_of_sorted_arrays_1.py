'''
Iteration 1
Time: 30 min
Problem: Sort two arrays and find median
'''


arr1 = [1,3,5]
arr2 = [2,4,6]
final_arr = []

for i in range(len(arr1)):
    if arr1[i] < arr2[i]:
        final_arr.append(arr1[i])
        final_arr.append(arr2[i])
    else:
        final_arr.append(arr2[i])
        final_arr.append(arr1[i])

print(final_arr)

if len(final_arr) % 2 != 0:
    middle = (len(final_arr) // 2) + 1
    median = final_arr[middle]
else:
    upper_mid = (len(final_arr) // 2) 
    lower_mid = (len(final_arr) // 2) - 1

    median = (final_arr[upper_mid] + final_arr[lower_mid]) / 2

print(median)