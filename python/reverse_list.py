my_list = [1,2,3,4]

def reverseList(a_list):
        start = 0
        end = len(a_list) - 1
        
        while start < end:
            temp = a_list[start]
            a_list[start] = a_list[end]
            a_list[end] = temp
            start += 1
            end -= 1
        return a_list

print(reverseList(my_list))

print("my list: " + str(my_list))

reversed(my_list)
# my_list.reverse()

print(my_list)