class SlidingWindowMedian:

  def find_sliding_window_median(self, nums, k):
    all_medians = []
    if len(nums) < k:
      return all_medians
    even = k % 2 == 0
    left = 0
    right = k

    while right <= len(nums):
      window = []
      for i in range(left, right):
        window.append(nums[i])
      window.sort()
      if not even:
        median = window[k//2]
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
