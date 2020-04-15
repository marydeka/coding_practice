'''
Permutations
'''

array = [1,2,3]

def perms(arr):
    if len(arr) == 0:
        return [[]]
    else:
        first_elem = arr[0]
        short_arr = arr[1:]
        short_arr_perms = perms(short_arr)
        result = []
        for perm in short_arr_perms:
            for i in range(len(perm) + 1):
                result.append(perm[0:i] + [first_elem] + perm[i:])

        return result

print(perms(array))

