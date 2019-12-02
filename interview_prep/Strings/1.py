"""
You are given a string containing characters A and B only. 
Your task is to change it into a string such that there are no matching adjacent characters. 
To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

For example, given the string s= AABAAB, remove A at positions 0 and 3 to make s = ABAB in 2 deletions.

Function Description:
It must return an integer representing the minimum number of deletions to make the alternating string.

alternatingCharacters has the following parameter(s):

    s: a string

"""

#my first working solution
def alternatingCharacters(s):
    #initialize count to 1 to account for the fact that at least one letter will always be kept
    count = 1
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            #increment count of chars to keep whenever a letter is different than the one after it
            count += 1
    #to find num deletions necessary, subtract the number of chars to keep from the length of string
    return (len(s) - count)

"""
A better solution that goes directly to counting number of deletions:

n = int(input())
for _ in range(n):
    count = 0;
    word = input()
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            count += 1
    print(count) 
"""