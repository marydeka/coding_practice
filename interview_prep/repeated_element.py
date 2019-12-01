"""
Leetcode 961. N-Repeated Element in Size 2N Array
Easy

In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

Example 1:

Input: [1,2,3,3]
Output: 3

Example 2:

Input: [2,1,2,5,3,2]
Output: 2
"""

def repeatedNTimes(A: List[int]) -> int:
    """
    First, calculate the target (number of times the element we're looking for is repeated).
        -Find length of array and divide by 2
    Create a dictionary to keep track of how many times each element is repeated.
    """
    
    target = len(A) / 2
    repeats = {}
    
    for num in A:
        if num not in repeats:
            repeats[num] = 1
        else:
            repeats[num] += 1
    
    for key in repeats.keys():
        if repeats[key] == target:
            return key
        
    return -1

print(repeatedNTimes([1,2,3,3]))
