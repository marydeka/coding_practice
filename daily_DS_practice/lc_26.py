'''
Leetcode 26: Remove Duplicates from Sorted Array
Level: Medium
Category: Arrays
Estimated Time Taken: 1 hr
'''

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        '''
        1. starting at index 1 and going until the last index, check to see if the num stored at previous index
        is the same. If so, check to see if num stored at next index is the same. Continue checking until the num is            different, and then set that num's index to be "next index"
        2. Essentially, swap out the repeated value for the new value
        '''
        
        # for i in range(1,len(nums) - 1):
        #     print("i: {}".format(i))
        #     for j in range(i + 1, len(nums)):
        #         print("     j: {}".format(j))
        
        end = len(nums) - 1
        for i in range(1,end):
            print("i: {}".format(i))
            if nums[i - 1] == nums[i]:
                for j in range(i + 1, len(nums)):
                    print("     j: {}".format(j))
                    if nums[j] != nums[i - 1]:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums.pop(nums[temp])
                        end -= 1
                        break
                        
        length = 1
        
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                length += 1
                
        return length