"""
Balanced Parentheses: Given an expression string, write a python program 
to find whether a given string has balanced parentheses or not.
"""

open_par = ["[","{","("] 
closed_par = ["]","}",")"] 

def check(str): 
    stack = [] 
    for i in str: 
        if i in open_par: 
            stack.append(i) 
        elif i in closed_par: 
            #the index function finds the index where the element first occurs
            pos = closed_par.index(i) 
            if ((len(stack) > 0) and
                #matching brackets are stored in the same positions in both lists
                (open_par[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"
  
# Tests
string = "{[]{()}}"
print(string,"-", check(string)) 
  
string = "[{}{})(]"
print(string,"-", check(string)) 