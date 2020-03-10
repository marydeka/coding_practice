'''
Iteration 2
Time: 16 min
Problem: Recursive approach to knapsack problem 

'''

def knapsack(profits, weights, capacity, index):
    #define base cases
    if len(profits) == 0 or len(weights) == 0:
        return 0
    if index > len(profits) - 1:
        return 0
    if weights[index] > capacity:
        return 0

    #recursive cases (include or skip weight at current index)
    profit1 = profits[index] + knapsack(profits, weights, capacity - weights[index], index + 1)

    profit2 = knapsack(profits, weights, capacity, index + 1)

    return max(profit1, profit2)






def main():
  print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7, 0))      #should return 22
  print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6, 0))       #should return 17


main()
