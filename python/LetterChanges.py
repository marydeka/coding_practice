def LetterChanges(str): 

    # code goes here 
    new_str = ""
    for char in str:
        if char.isalpha():
            if char == 'z' | 'Z' #this line gave error on coderbyte, not sure why
               char = 'A'
            else:
                char = chr(ord(char) + 1)
            if char in 'aeiou':
                char = char.upper()
        
        new_str = new_str + char
        
    return new_str
    
# keep this function call here  
print LetterChanges(raw_input())  