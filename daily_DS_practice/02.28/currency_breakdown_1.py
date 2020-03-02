'''
Iteration 1 (looks like there's a bug somewhere)

Given input B (balance), W (withdrawal amount), N (number of packets), and P (ml packet sizes), 
give the output for the amount of each packet provided and the remaining balance,
in ratio format from smallest to largest packets along with remaining account balance.

If not enough balance, output "Not enough balance." If the balance can't be broken into 
available packets, output "cannot put into packets"

Input format:
B W N
P

Read from standard input

Sample input:  --> True, 1:2 1:5 1:10 1:50 5:100 433
1000 567 5
2
5
10
50
100
'''

#Note to self: cannot simply use greedy algorithm since the packet sizes might not work for this

inputs = [1000, 567, 5]
packets = [2, 5, 10, 50, 100]
max_packets = 5
withdrawal = 567
DEBUG = True


#if withdrawal == 0 and max(times_used) <= max_packets   doesn't work but it should!

def is_able_to_split(withdrawal, packets, times_used, max_packets, level):
    string = "    " * level
    if DEBUG:
        print(f"{string} withdrawal:{withdrawal}, times_used: {times_used}, level: {level}")
    if withdrawal == 0:
        return True
    elif withdrawal < 0: 
        return False
    elif max(times_used) > max_packets:
        return False
    else:
        answer = False
        for index, curr_packet in enumerate(packets):
            updated_times_used = times_used.copy()
            updated_times_used[index] += 1
            answer =  answer or is_able_to_split(withdrawal - curr_packet, packets, updated_times_used, max_packets, level + 1)
            if answer:
                break
        return answer



# times_used = [0 for packet in packets]

# print(is_able_to_split(567, packets, times_used, max_packets, 1))

print(is_able_to_split(10, [2,7], [0,0], 5, 1))  # should return True


