"""
Alice wrote a sequence of words in CamelCase as a string of letters, s,
having the following properties:

    It is a concatenation of one or more words consisting of English letters.
    All letters in the first word are lowercase.
    For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.

Given s, print the number of words in s on a new line.

For example, s= oneTwoThree. There are 3 words in the string. 
"""

def camelcase(s):
    count = 0

    if len(s) == 0:
        return count
    else:
        #if the string isn't empty, there is at least one word
        count += 1
        for char in s:
            #numbers representing uppercase letters are less than lowercase letters
            if char < 'a':
                #every time we find an uppercase letter, it represents a new word
                count += 1
    return count