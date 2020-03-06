def get_shortest_unique_substring(arr, string):
  tail = 0 
  head = 0
  unique = 0
  letter_counts = {}
  for letter in arr:
      letter_counts[letter] = 0
      
  results_substr = ""
  
  
  while tail < len(string):
    tail_char = string[tail]
    if (tail_char not in letter_counts):
      continue
    
    tailCount = letter_counts[tail_char]
    if (tailCount== 0):
      unique += 1
    
    letter_counts[tail_char] += 1
    
    while (unique == len(arr)):
      tempLength = tail - head + 1
      if tempLength == len(arr):
        return string[head:tail+1]
      if (results_substr == "" or tempLength < len(results_substr)):
        results_substr = string[head:tail+1]
      
      head = string[head]
      
      if (head in letter_counts):
        letter_counts[head] -= 1
        if letter_counts[head] == 0:
          unique -= 1
          
      head += 1
      
  return result
  
  '''
  while tail < len(string):
    flag = True
    curr = string[head]
    if curr in letter_counts:
      letter_counts[curr] += 1
    for letter in letter_counts.keys():
      if letter_counts[letter] < 1:
        flag = False
    substr = string[tail: head + 1]
    if flag == True and len(substr) < len(result_substr):
      results_substr = substr
      
    else:
      
      head += 1
  
  '''
  
      
      
  if len(results_substr) < len(string) + 1:
    return results_substr
  else:
    return ""
      
      
  
  
'''

1. create dictionary of letter counts
2. move head pointer until each letter in arr has count of at least 1
3. save substring in results variable
4. move tail pointer (update dictionary) and head pointer within while loop
5. while loop ends if tail pointer can't be incremented
6. while loop keeps updating substring if new substring is smaller
7. return substring

input:  arr = ['x','y','z'], str = "xyyzyzyx"

output: "zyx"
'''
