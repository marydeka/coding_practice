def validNumber(self, num):

    num_digits = int(math.log10(num)) + 1

    str_num = str(num)

    for digit in range(num_digits):
        if digit == 0:
            return False
        elif num % int(str_num[digit]) != 0:
            return False
    
    return True

print(validNumber(3)) 