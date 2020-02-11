'''
AlgoDaily: Power of Three
Level: Easy
Date: Feb 10
'''


def powerOfThree(num):
    if num / 3 == 1:
        return True
    elif num / 3 < 3:
        return False
    else:
        return powerOfThree(num/3)

#TEST 1     should return True

print(powerOfThree(9))

#TEST 2     should return False
print(powerOfThree(15))

#TEST 3     should return True
print(powerOfThree(729))