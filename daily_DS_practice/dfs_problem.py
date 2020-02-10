
# matrix = [[1,0,1,0],[1,0,1,0],[0,1,1,0]]        #should print 2
matrix = [[1,1,0,0,1,1],[0,0,1,1,0,1],[0,0,0,1,1,0],[1,0,1,0,0,0]]   #should print 5

def count_islands(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
        #     print(matrix[i][j], end = "")
        # print('\r')
            if matrix[i][j] == 1:
                count += 1
                mark_visited(i, j, rows, cols)

    return count
                

    # for i in range(rows):
    #     for j in range(cols):
    #         print(matrix[i][j], end = "")
    #     print('\r')

def mark_visited(i, j, num_rows, num_cols):     #do I need to pass in matrix as well here? and for is_valid?
    #check to make sure that i and j are valid indices
    if is_valid(i,j, num_rows, num_cols):
        print(f"i: {i}, j: {j}")
        if matrix[i][j] == 1:
            matrix[i][j] = -1
            mark_visited(i, j - 1, num_rows, num_cols)
            mark_visited(i, j + 1, num_rows, num_cols)
            mark_visited(i - 1, j, num_rows, num_cols)
            mark_visited(i + 1, j, num_rows, num_cols)
    


def is_valid(i,j, num_rows, num_cols):
    if i >= 0 and i < num_rows and j >= 0 and j < num_cols:
        return True
    else:
        return False

print(count_islands(matrix))
