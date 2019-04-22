def LongestWord(sen): 

    # code goes here 
    sen = sen.translate(None, "~!@#$%^&*()-_+={}[]:;'<>?/,.|`")
    array = sen.split(" ")
    return max(array, key=len)
    
# keep this function call here  
print LongestWord(raw_input())