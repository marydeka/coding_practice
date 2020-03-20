'''
Iteration 2
Time: Over 2 hrs
Problem: Dynamic Programming Knapsack
'''

'''
Iteration 3:
Time: 55 min
Problem: Knapsack Dynamic Programming
'''

def knapsack(profits, weights, capacity):
    #create matrix to store all possible profits
    matrix = [[0 for capacity in range(capacity + 1)] for weight in weights]
    # print(matrix)

    #when capacity is zero, profit is zero, so first column stays zero

    #when we only have one weight, if it's less than/equal to capacity, then profit is profit at that index
    for j in range(capacity + 1):
        if weights[0] <= j:
            matrix[0][j] = weights[0]
    # print(matrix)

    #fill in rest of matrix by taking max of including weight or not including weight
    
    
    for i in range(len(weights)):
        for c in range(capacity + 1):

            #can only include profit at current index if weight at curr index is <= capacity in matrix
            profit1 = 0
            if weights[i] <= c:
                # print("i: " + str(c - weights[i]))
                # print("c: " + str(c))
                profit1 = profits[i] + matrix[i - 1][c - weights[i]]

            #exclude current weight/profit by taking whatever number fit capacity in prev row
            profit2 = matrix[i - 1][c]

            matrix[i][c] = max(profit1, profit2)

    # print(matrix)
    # print("cap: " + str(capacity))
    return matrix[len(weights) - 1][capacity]

def main():
  print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5)) #should print 16
  print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))  #should print 17
  print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))  #should print 22


main()