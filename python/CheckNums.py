#coderbyte: check to see if the numbers are equal, or if one is greater than the other

def CheckNums(num1,num2):
    if num2 > num1:
        return "true"
    elif num2 < num1:
        return "false"
    return "-1"
print CheckNums(raw_input())