"""
Leetcode 1207. Unique Number of Occurrences
Easy

Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:

Input: arr = [1,2]
Output: false

Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

Constraints:

    1 <= arr.length <= 1000
    -1000 <= arr[i] <= 1000
"""

def uniqueOccurrences(self, arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    
    """
    
    
    
    """
    
    counts = {}
    
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
            
    #check to see if each value stored in counts is unique
    num_occurrences = {}
    
    for value in counts.values():
        if value in num_occurrences:
            return False
        else:
            num_occurrences[value] = 1
    return True

print(uniqueOccurrences([1,2,2,1,1,3]))