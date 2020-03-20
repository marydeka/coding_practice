matrix = [[1,2,3], [4,5,6], [7,8,9]]


i = 0
j = 0
nums_to_multiply = []

nums_to_multiply.append(matrix[i][j])

while i < len(matrix) and j < len(matrix[0]):
    if matrix[i + 1][j] > matrix[i][j + 1]:
        nums_to_multiply.append(matrix[i + 1][j])
    else: 
        nums_to_multiply.append(matrix[i][j + 1])
