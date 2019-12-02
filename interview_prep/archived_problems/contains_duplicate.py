"""
Leetcode 219: Easy

Given an array of integers and an integer k, find out whether 
there are two distinct indices i and j in the array such that nums[i] = nums[j] 
and the absolute difference between i and j is at most k."""

# class Solution(object):


def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    helper_map = {}
    for i, num in enumerate(nums):
        if num in helper_map and i - helper_map[num] <= k:
            return True
        helper_map[num] = i
    return False

print(containsNearbyDuplicate([1,2,3,1], 3))