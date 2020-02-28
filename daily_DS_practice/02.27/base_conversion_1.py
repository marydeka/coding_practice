'''
Iteration 1

Given an input string composed of 0-9 and a-z, determine
which base to convert the string to in order to get the smallest number
and then convert that number to base 10

Note: the number is positive and will never start with zero

Sample input: "cats" --> 75  (convert cats to base 4 (1023) and then to base 10)
Sample input: "11001001" --> 201
Sample input = "ab2ac999"  #should produce 85499
Sample input = "abcdefghijklmnop" --> 1162849439785405935
'''


input = "ab2ac999"

input = list(input)

#count unique characters to determine base

letters = set()
for char in input:
    letters.add(char)

print(letters)

base = len(letters)

second_num_occurred = False

letter_dict = {}

output_list = []

num = 1

for char in input:
    if char in letter_dict:
        continue
    #the second character should be given a 0, since the first cannot
    elif second_num_occurred == False and num == 2:
        letter_dict[char] = 0
        second_num_occurred = True
    else:
        letter_dict[char] = num
        num += 1

print(letter_dict)

for char in input:
    output_list.append(str(letter_dict[char]))

print(output_list)

#now convert output string to base 10

base_ten_sum = 0
multiple = 0
# for char in reversed output string
for char in output_list[::-1]:
    base_ten_sum += int(char) * base**multiple
    multiple += 1
print(base_ten_sum)
print(base)
