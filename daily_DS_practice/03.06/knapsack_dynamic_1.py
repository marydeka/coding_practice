def solve_knapsack(profits, weights, capacity):
  #base cases
  if capacity <= 0 or len(profits) == 0:
    return 0

  length = len(profits)

  #initialize matrix to store profits
  matrix = [[0 for j in range(capacity + 1)] for i in range(length)]
  # print(matrix)

  #can initialize first row by determining if the single weight 
  #is less than or equal to the current capacity
  for c in range(1, capacity + 1):
    if weights[0] <= capacity:
      matrix[0][c] = profits[0]

  #when the capacity is zero, we know that our max profit is zero
  #and we've already initialized first row,
  #so we'll start our main iteration through the matrix
  #from when capacity is equal to 1 and index is equal to 1
  for i in range(1, length):
    for c in range(1, capacity + 1):

      #including the weight at the current index
      profit1 = 0
      if weights[i] <= c:
        weight_added = weights[i]
        profit1 = profits[i] + matrix[i - 1][c - weight_added]


      #excluding the weight at the current index
      profit2 = matrix[i - 1][c]

      matrix[i][c] = max(profit1, profit2)

  #greatest profit will be stored in bottom right corner
  return matrix[length - 1][capacity]




def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5)) #should print 16
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))  #should print 17
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))  #should print 22


main()

