'''
Problem: Consecutive Array
Time: 1 hr
Iteration: 2
'''

# consec = [4,2,1,6,5]
consec = [5,5,3,1]
longest_length = 1
length = 1
consec_nums = []

if len(consec) == 0:
    print('[]')

consec.sort()

left = 0
right = 1

consec_nums.append(consec[left])

while right < len(consec):
    # print(f"right: {right}")
    # print(f"left: {left}")
    if consec[right] - consec[left] == 1:
        consec_nums.append(consec[right])
        length += 1
        right += 1
        left += 1
        # print(f"current length: {length}")
    else: 
        length = 1
        left = right
        consec_nums = []
        consec_nums.append(consec[left])
        right += 1
        # print(f"current length: {length}")
    if length > longest_length:
        # print("entered")
        longest_length = length

print(longest_length)
print(consec_nums)