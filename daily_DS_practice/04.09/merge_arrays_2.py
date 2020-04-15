'''
Problem: Merge arrays
'''


A = [1,3,5,0,0,0]
B = [2,4,6]

insert = len(A) - 1
ptr_A = len(A) - 1
ptr_B = len(B) - 1

while A[ptr_A] == 0 and ptr_A >= 0:
    ptr_A -= 1

# print(ptr_A)
# print(ptr_B)

while insert >= 0:
    # if ptr_B < 0:
    #     A[insert] = A[ptr_A]
    #     ptr_A -= 1
    # elif ptr_A < 0:
    #     A[insert] = B[ptr_B]
    #     ptr_B -= 1

    if B[ptr_B] > A[ptr_A] and ptr_B >= 0:
        A[insert] = B[ptr_B]
        ptr_B -= 1

    elif A[ptr_A] > B[ptr_B] and ptr_A >= 0:
        A[insert] = A[ptr_A] 
        ptr_A -= 1
    insert -= 1

print(A)
