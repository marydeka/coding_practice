'''

Grokking: Sliding Window Median (hard)
https://www.educative.io/courses/grokking-the-coding-interview/3Y9jm7XRrXO

Iteration 1 (next time try using max and min heaps)
'''

class SlidingWindowMedian:

  def find_sliding_window_median(self, nums, k):
    result = []
    if len(nums) < k:
      return result
    left = 0
    right = k - 1
    while right < len(nums):
      sum_of_window = 0
      list_of_nums = []
      for i in range(left, right + 1):
        list_of_nums.append(nums[i])
        list_of_nums.sort()
        print(list_of_nums)
        #if k is odd, median is middle number
      if k % 2 != 0:
        median_index = len(list_of_nums)//2
        median = list_of_nums[median_index]
        result.append(median)
      else:
        #if k is odd, median is the mean of the two middle numbers
        upper_middle_index = len(list_of_nums) // 2
        lower_middle_index = upper_middle_index - 1
        median = (list_of_nums[upper_middle_index] + list_of_nums[lower_middle_index]) / 2
        result.append(median)
      left += 1
      right += 1

    return result

def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()
