import math
import os
import random
import re
import sys

#this function checks to see that all characters occur either 1 time, or, at max, one character can appear twice

def isValid(s):

    my_dict = {}
    extra_occurrence = False

    for char in s:
        if char not in my_dict:
            #Note: had accidentally set this to my_dict[char] == 1, which led to KeyError
            my_dict[char] = 1


        elif char in my_dict:
            if my_dict[char] > 2:
                return False 
            elif my_dict[char] == 1 and extra_occurrence == True:
                return False
            elif my_dict[char] == 1 and extra_occurrence == False:
                my_dict[char] += 1
                extra_occurrence = True

    return True

print(isValid("abc"))


#second version of problem

"""

Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
It is also valid if he can remove just character at index in the string, and the remaining characters will occur the same number of times. 
Determine if string is valid. If so, return YES, otherwise return NO.

"""

def isValid2(s):
    if len(s) == 0:
        return "YES"

    dict = {}
    #keep track of if we have already found a difference in frequency of 1
    difference = False

    for char in s:
        if char not in dict:
            dict[char] = 1

        elif char in dict:
            dict[char] += 1

    #every value in dict needs to either equal the same thing, or have at most one difference
    val_to_test = dict[s[0]]

    for val in dict.values():
        if val != val_to_test and difference == False:
            if abs(val - val_to_test) == 1:
                difference = True
            else:
                return "NO"
        elif val != val_to_test and difference == True:
            return "NO"

    return "YES"