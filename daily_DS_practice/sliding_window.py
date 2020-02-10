import sys

string = "twcpblmabccabasdcbasaasbacccbajkhca"
target = ['a', 'b', 'c']

#initialize trailing point
j = 0
shortest_length = sys.maxsize

#current character counts of each character in target
char_counts = {}

for char in target:
    char_counts[char] = 0

# print(char_counts)

#i is my leading pointer
for i in range(len(string)):
    if string[i] in char_counts:
        # print(f"i: {i}")
        char_counts[string[i]] += 1
        # print(char_counts)
        # print(f"min char count: {min(char_counts.values())}")

        if min(char_counts.values()) > 0:
            # print(f"after finding min to be 1: {char_counts}")
            #continue incrementing trailing pointer to see how much substring can be shortened
            while min(char_counts.values()) != 0: 
                # j += 1
                # print(f"j in while loop: {j}")
                if string[j] in char_counts:
                    char_counts[string[j]] -= 1
                    if min(char_counts.values()) == 0:
                        new_length = abs(j - i) + 1
                        if new_length < shortest_length:
                            shortest_length = new_length
                            print(f"-------------------->>>>>>>>>>>>i: {i}, j: {j}, substr: {string[j: i + 1]}")
                
                j += 1  
            print(string[j - 1: i])          



# print(f"    j: {j}")
# print(char_counts)