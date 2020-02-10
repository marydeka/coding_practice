# def find_num_combos(dollar_amount, coin_list):
#     total_num_combos = 0
#     if dollar_amount in coin_list:
#         return 1
#     elif dollar_amount < min(coin_list):
#         return 0
#     else:
#         for i in range(len(coin_list)):
#             total_num_combos += find_num_combos(dollar_amount - coin_list[i], coin_list)
#         return total_num_combos

# print(find_num_combos(15, [1,5]))  #should print 4


def find_num_combos(dollar_amount, coin_list):
    total_num_combos = 0
    if dollar_amount in coin_list:
        return [[dollar_amount]]
    elif dollar_amount < min(coin_list):
        return []
    else:
        for i in range(len(coin_list)):
            total_num_combos += find_num_combos(dollar_amount - coin_list[i], coin_list)
        return total_num_combos

print(find_num_combos(6, [1,2,5]))  #should print 4