#coderbyte: return the hour and minutes from input

def TimeConvert(num): 

    # code goes here 
    
    return (str(num / 60) + ":" + str(num % 60))
    
# keep this function call here  
print TimeConvert(raw_input())