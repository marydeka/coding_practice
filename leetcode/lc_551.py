'''
Leetcode 551: Student Attendance Record I
Level: Easy
Category: Strings
Estimated Time Taken: 10 minutes
'''


class Solution:
    def checkRecord(self, s: str) -> bool:
        A_count = s.count('A')
        
        #only enter loop if there are 1 or fewer A's
        if A_count <= 1:
            #keep track of how many times L appears consecutively
            L_count = 0
            for char in s:
                if char == 'L':
                    L_count += 1
                    if L_count > 2:
                        return False
                elif char != 'L':
                    L_count = 0
        else:
            return False
                    
        return True