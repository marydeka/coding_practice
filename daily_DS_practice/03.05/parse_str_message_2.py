'''
Iteration 2
Time: 

Current year: 2017

< means go back one year
> means go forward one year 
* doubles the effect of the char two positions before this char
(if * points to another *, it doubles effect of existing multiplication)

Determine what the final year is.
'''

symbols = {'<': -1, '>': 1}
string = "<<<*>>*<*<<"
start_year = 2017
multiplier = 2
list_of_nums = list(string)

for index in range(len(list_of_nums) - 1, -1, -1):
    print(start_year)
    char = list_of_nums[index]
    if char in symbols:
        start_year += symbols[char]
    elif char == '*' and (index - 2) >= 0:
        if list_of_nums[index - 2] != '*':
            if list_of_nums[index - 2] in symbols:
                char = symbols[list_of_nums[index - 2]]
            else:
                char = list_of_nums[index - 2]
            start_year += multiplier * char
        else: 
            curr_index = index
            while list_of_nums[curr_index - 2] == '*':
                multiplier *= 2
                curr_index -= 2

            list_of_nums[curr_index - 2] = multiplier * symbols[list_of_nums[curr_index - 2]]
            multiplier = 2

print(start_year)
