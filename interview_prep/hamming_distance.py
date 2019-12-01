"""
Leetcode 461. Hamming Distance
Easy

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

"""

def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    
    """
    -Initialize a count variable.
    -Convert each decimal value into its binary value.
    Do a xor operation on each comparison of values,
    and each time it's true, increment the count.
    """


    return bin(x^y)[2:].count("1")

print(hammingDistance(1,4))