matrix = [[True, False, False], [False, False, False], [False, False, False]]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == True:
            print(f"i: {i}, j: {j}")
            #set all of the elements in that same column to True
            for k in range(i + 1, len(matrix)):
                print(f"k: {k}")
                matrix[k][j] = "change"
            #set all elements in that same row to True
            for l in range(j + 1, len(matrix[0])):
                print(f"l: {l}")
                matrix[i][l] = "change"

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "change":
            matrix[i][j] = True


print(matrix)