'''
Iteration 3
Time: 35 min 
Problem: Knapsack Recursive

'''

def knapsack(profits, weights, capacity, index, level):

    multiplier = "     "

    #define base cases
    if len(profits) == 0 or len(weights) == 0:
        return 0
    if capacity <= 0:
        return 0
    if index >= len(profits):
        return 0
    if weights[index] > capacity:
        return 0

    #define recursive cases (count the current weight or don't)
    profit1 = knapsack(profits, weights, capacity, index + 1, level + 1)
    print(multiplier * level + str(level) + ":profit 1: " + str(profit1))

    profit2 = profits[index] + knapsack(profits, weights, capacity - weights[index], index + 1, level + 1)

    return max(profit1, profit2)



def main():
  print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7, 0, 0))      #should return 22
  print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6, 0, 0))       #should return 17


main()