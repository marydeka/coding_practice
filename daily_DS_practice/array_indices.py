'''
Using two pointers method to save space
Time Complexity: O(n)
Space Complexity: O(n)
'''

#TEST CASE 1: should return [1, 3]
# arr = [1,3,6,7,9]
# goal = 10

#TEST CASE 2: should return [0,2]
# arr = [1,5,18]
# goal = 19

# left = 0
# right = len(arr) - 1 

# while left < right:
#     if arr[left] + arr[right] == goal:
#         # print("entered")
#         print(f"answer: {[left, right]}") 
#         break
#     elif arr[left] + arr[right] > goal:
#         right -= 1
#     elif arr[left] + arr[right] < goal:
#         left += 1



'''
Using dictionary
Time Complexity: O(n)
Space Complexity: O(n) 
'''

#TEST CASE 1: should return [0,2]
# arr = [1,6,9,7,3]
# goal = 10

#TEST CASE 2: should return [1,3]
# arr = [8,5,4,9]
# goal = 14

# #TEST CASE 3: should return [0,1]
# arr = [1,9,13,20,47]
# goal = 10

#TEST CASE 4: should return []
arr = []
goal = 10

num_dict = {}
for index, num in enumerate(arr):
    num_dict[num] = index

# print(num_dict)
if len(arr) == 0:
    print(f"answer: {[]}")

for index, num in enumerate(arr):
    if goal - num in num_dict:
        print(f"answer: {[index, num_dict[goal - num]]}")
        break