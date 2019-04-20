#coderbyte: capitalize the first letter in each word of a string
#also realized later that there's a function str.title() that does this

def LetterCapitalize(str): 

    # code goes here 
    array = str.split(" ")
    
    for i in range(0, len(array)):
        array[i] = array[i][0].upper() + array[i][1:]
        
    return " ".join(array)
    
# keep this function call here  
print LetterCapitalize(raw_input())