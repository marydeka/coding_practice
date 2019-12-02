"""
Leetcode 905. Sort Array By Parity
Easy

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

"""

def sortArrayByParity(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    
    """
    First, select all even elements of array and add them to array "evens".
    Second, select all odd elements of array and add them to array "odds"
    Return the concatenation of these two arrays.
    """
    
    odds = []
    evens = []
    
    for i in range(len(A)):
        if A[i] % 2 == 0:
            evens.append(A[i])
        else:
            odds.append(A[i])
            
    return evens + odds

print(sortArrayByParity([3,1,2,4]))