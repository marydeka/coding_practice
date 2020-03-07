'''
Iteration 2
Time: 1.5 hours
Problem: Shortest Substring (sliding window)

'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""
        
        left = 0
        right = 0
        counts = {}
        all_chars_present = False
        shortest_substr = None
        substr = None
        
        for char in t:
            counts[char] = 0
        
        while right < len(s):
            while right < len(s):
                char = s[right]
                print("right pointer points to: " + str(char))
                if char in counts:
                    counts[char] += 1
                all_chars_present = True
                for count in counts.values():
                    if count == 0:
                        all_chars_present = False
                        break
                if all_chars_present == False:
                    right += 1
                # else:
                #     print("entered else")
                #     break
                if all_chars_present == True:
                    break

            #keep shrinking window until substring isn't valid
            while all_chars_present == True and left <= right and right < len(s):
                print("entered")
                char = s[left]
                if char in counts:
                    counts[char] -= 1
                for count in counts.values():
                    if count == 0:
                        all_chars_present = False
                left += 1
                substr = s[left - 1: right + 1]
                print(substr)

            
            if substr:
                if len(substr) == len(t):
                    return substr
                elif shortest_substr == None:
                    shortest_substr = substr
                elif len(substr) < len(shortest_substr):
                    shortest_substr = substr

            right += 1
        
        if shortest_substr == None:
            return ""
        return shortest_substr
        
            
            

      
    
    
   



