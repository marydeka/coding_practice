'''
Iteration 1
Time: More than 2 hrs
Problem: Matrix product (byte-by_byte)
'''


matrix = [[1,2,3], [4,5,6], [7,8,9]]


i = 0
j = 0
nums_to_multiply = []

nums_to_multiply.append(matrix[i][j])

while i < len(matrix) and j < len(matrix[0]):
    # nums_to_multiply.append(max(matrix[i +1][j]), matrix[i][j + 1])
    if matrix[i + 1][j] > matrix[i][j + 1]:
        nums_to_multiply.append(matrix[i + 1][j])
        i += 1
    else: 
        nums_to_multiply.append(matrix[i][j + 1])
        j += 1

total_sum = 1
for num in nums_to_multiply:
    total_sum *= nums_to_multiply

print(total_sum)
