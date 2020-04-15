'''
Problem Iteration: 1
Problem: Square Submatrix
Time: More than 2 hrs
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        largest_square = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # print(f"i: {i}, j: {j}")
                curr_largest_square = 0
                if matrix[i][j] == "1":
                    # print(f"i: {i}, j: {j}")
                    i_start = i
                    j_start = j
                    # print("entered first if")
                    curr_largest_square = 1
                    iteration = 1
                    
                    while i_start + 1 < len(matrix) and j_start + 1 < len(matrix[0]) and matrix[i_start + 1][j_start + 1] == "1":
                        print(f"i_start: {i_start}, j_start: {j_start}")
                        #have to check to see if every new square has 1 in it
                        for num in range(i_start, i_start + 2):
                            if matrix[num][j_start + 1] == "0":
                                break
                            if matrix[i_start + 1][num] == "0":
                                break
                        
                        
                        iteration += 1
                        curr_largest_square = iteration**2
                        print(curr_largest_square)
                        
                        #have to increment i_start and j_start
                        i_start += 1
                        j_start += 1

                if curr_largest_square > largest_square:
                    largest_square = curr_largest_square
                            
        return largest_square
                                
                            