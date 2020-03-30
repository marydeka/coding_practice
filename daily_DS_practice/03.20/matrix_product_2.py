'''
Iteration 2
Time: 
'''

matrix = [[1,2,3],[1,2,1][7,1,1]]
start = matrix[0][0]
end = matrix[len(matrix) - 1][len(matrix[0]) - 1]

i = 0
j = 0
product = 1

def find_max_product(matrix, i, j):
    #define base cases

    if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
        return product * matrix[i][j]

