'''
Iteration 2
Time: Over 2 hrs
Problem: Dynamic Programming Knapsack
'''


def knapsack(profits, weights, capacity):
    if len(weights) == 0 or len(profits) == 0:
        return 0
    if capacity <= 0:
        return 0

    #initialize matrix with all 0s
    max_profits = [[0 for num in range(capacity + 1)] for num in range(len(profits))]
    # print(max_profits)

    #first column will be all zeroes (since capacity is zero)
    #first row will be whatever the weight is at the 0th index (if less than or equal to that particular capacity)

    for i in range(len(profits)):
        max_profits[i][0] = 0

    for j in range(capacity + 1):
        if weights[0] <= j:
            max_profits[0][j] = weights[0]

    #fill in rest of matrix by picking max of two profits (including or excluding current weight)
    for i in range(1, len(profits)):
        print(f"i: {i}")
        for cap in range(1, capacity + 1):
            print(f"cap: {cap}")

            profit1 = 0  
            if weights[i] <= cap:
                profit1 = profits[i] + max_profits[i-1][cap - weights[i]]

            profit2 = max_profits[i - 1][cap]

            max_profits[i][cap] = max(profit1, profit2)


    #return the greatest profit, which will be stored in bottom right corner
    print(max_profits)
    return max_profits[len(profits) - 1][capacity]







def main():
  print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5)) #should print 16
  print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))  #should print 17
  print(knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))  #should print 22


main()