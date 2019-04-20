#coderbyte: return the alphabetized string

def AlphabetSoup(str): 

    # code goes here 
    s = list(str)
    s.sort()
    return ''.join(s)
    
# keep this function call here  
print AlphabetSoup(raw_input())