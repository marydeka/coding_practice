'''
Iteration 3
Time: 13 min
Link to problem: https://www.educative.io/courses/grokking-the-coding-interview/3Y9jm7XRrXO
'''


class SlidingWindowMedian:

  def find_sliding_window_median(self, nums, k):
    all_medians = []

    left = 0
    right = k - 1

    while right < len(nums):
      window = []
      #create new window (list) in which to find median
      for i in range(left, right + 1):
        window.append(nums[i])
      window.sort()
      if k % 2 != 0:
        median = float(window[k//2])
      else:
        upper_middle = k // 2
        lower_middle = upper_middle - 1
        median = (window[upper_middle] + window[lower_middle]) / 2
      all_medians.append(median)

      left += 1
      right += 1

    return all_medians



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
