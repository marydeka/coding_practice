'''
Iteration 2
Time: around 1 hr, 40 min

Current year: 2017

< means go back one year
> means go forward one year 
* doubles the effect of the char two positions before this char
(if * points to another *, it doubles effect of existing multiplication)

Determine what the final year is.

'''

def get_result_year(string):
    DEBUG = False
    current_year = 2017
    result_year = current_year

    symbols = {'>': 1, '<': -1}

    #reverse the string and iterate through forwards

    new_str = ""
    for char in string:
        new_str = char + new_str
    if DEBUG: print(f"original string: {string}")
    if DEBUG: print(new_str)

    #make string an array so it can be modified
    string_list = list(new_str)
    sum_to_add = 0
    multiplier = 2
    for i in range(len(string_list)):
        if DEBUG: print(f"i: {i}")
        if string_list[i] in symbols:
            sum_to_add += symbols[string_list[i]] 
        elif string_list[i] == '*':
            if i + 2 < len(string_list):
                if string_list[i + 2] == '*':
                    multiplier *= 2
                elif string_list[i + 2] in symbols:
                    print(string_list[i + 2])
                    string_list[i + 2] = multiplier * symbols[string_list[i + 2]]

        #if this element has been modified
        else:
            if DEBUG: print(sum_to_add)
            if DEBUG: print(string_list[i])
            sum_to_add += string_list[i]
        if DEBUG: print(f"new sum: {sum_to_add}")

    if DEBUG: print(sum_to_add)

    result_year += sum_to_add

    print(result_year)






get_result_year('>><<>>*><')
