string1 = "{[1+2](7%3}" #should return False (brackets not matched)
string2 = "{[7 + (3 - 1)] + [(4 +1)]}"  #should return True


def match_brackets(string):
    o = {'{': 0, '(': 1, '[': 2}
    c = {'}':0, ')': 1, ']': 2}

    stack = []

    for char in string:
        #only pay attention to open and closed braces
        if (char in o) or (char in c):
            #if stack is empty, only an open brace can be added
            if len(stack) == 0:
                if char not in o:
                    return False
                else:
                    stack.append(char)
            else:
                #peek at the top character in stack
                top = stack[-1]
                if top in o and char in o:
                    stack.append(char)
                elif top in o and char in c:
                    #if the values for top and char in those dicts aren't the same, they don't match; string isn't valid
                    if o[top] != c[char]:
                        return False
                    else:
                        #if the values for top and char do match, then they cancel each other 
                        stack.pop()

    return True

print(match_brackets(string1))
print(match_brackets(string2))