def get_shortest_unique_substring(t, s):      
      if len(t) > len(s):
        return ""
    
      substr = None
      shortest_substr = None
      left = 0
      right = 0
      counts = {}
      all_chars_present = False   #True when all counts are greater than zero

      for char in t:
        counts[char] = 0

      print(counts)
    
      while right < len(s):
        while all_chars_present == False and right < len(s):
            
            if s[right] in counts:
              char = s[right]
              counts[char] += 1
            all_chars_present = True
            for count in counts.values():
              if count == 0:
                all_chars_present = False 
                
            print(all_chars_present)
                
            if all_chars_present == False:  
              right += 1
              print(right)
            else:
              break
                
        print(right)
        print(all_chars_present)
        while all_chars_present:
            char = s[left]
            if char in counts:
                counts[char] -= 1
            left += 1

            all_chars_present = True
            for count in counts.values():
              if count == 0:
                all_chars_present = False 


            substr = s[left - 1: right + 1]
            print(substr)
        
        if substr:
            if len(substr) == len(t):
                return substr
            elif not shortest_substr:
                shortest_substr = substr
            elif len(substr) > len(t) and len(substr) < len(shortest_substr):
                shortest_substr = substr



            print(substr)
        right += 1
            
      if shortest_substr:
        return shortest_substr
      else:
        return ""
    
        

      
    
    
   





   



