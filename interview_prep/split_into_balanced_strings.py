"""
Leetcode 1221. Split a String in Balanced Strings
Easy

Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

"""

def balancedStringSplit(self, s):
    """
    :type s: str
    :rtype: int
    """
    
    balance = 0
    count = 0
    
    for char in s:
        if char == 'L':
            balance += 1
        if char == 'R':
            balance -= 1
        if balance == 0:
            count += 1
    return count

print(balancedStringSplit("RLRRLLRLRL"))
