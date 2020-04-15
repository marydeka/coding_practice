'''
Iteration 1
Time: 1 hour and 30 min
Problem: Knapsack Recursive
'''


def knapsack_recursive(profits, weights, capacity, index):
  # base cases
  if capacity <= 0 or index >= len(profits):
    return 0

  # recursive call after choosing the element at the current index
  # if weight of element at current index is greater than the capacity, then don't include it
  profit1 = 0
  if weights[index] <= capacity:
    profit1 = profits[index] + knapsack_recursive(
      profits, weights, capacity - weights[index], index + 1)

  # recursive call after excluding element at the current index
  profit2 = knapsack_recursive(profits, weights, capacity, index + 1)

  return max(profit1, profit2)


def main():
  print(knapsack_recursive([1, 6, 10, 16], [1, 2, 3, 5], 7, 0))     #should return 22
  print(knapsack_recursive([1, 6, 10, 16], [1, 2, 3, 5], 6, 0))     #should return 17


main()

