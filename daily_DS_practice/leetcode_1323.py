'''
Leetcode 1323: Maximum 69 Number
Level: Easy
Category: Strings
Estimated Time Taken: 15 minutes
'''

class Solution:
    def maximum69Number (self, num: int) -> int:
        #iterate through list to find first 6 and change it to a nine
        list_num = [digit for digit in str(num)]
        print(list_num)
        
        for i, digit in enumerate(list_num):
            # print(f"i: {i}")
            # print(f"digit: {digit}")
            if digit == '6':
                # print("entered")
                # print(list_num)
                list_num[i] = '9'
                # print(list_num)
                break
                
        return int("".join(list_num))