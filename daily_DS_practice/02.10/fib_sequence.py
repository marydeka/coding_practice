#parameter passed in means we need to find the nth fibonacci number

def fib_sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_sequence(n - 1) + fib_sequence(n - 2)


#TEST 1: should return 1
print(fib_sequence(1))

#TEST 2: should return 1597
print(fib_sequence(17))

#TEST 3: should return 5702887
print(fib_sequence(34))