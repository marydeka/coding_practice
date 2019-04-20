'''
#coderbyte: Have the function KaprekarsConstant(num) take the num parameter 
being passed which will be a 4-digit number with at least two distinct 
digits. Your program should perform the following routine on the number:
Arrange the digits in descending order and in ascending order 
(adding zeroes to fit it to a 4-digit number), and subtract the smaller 
number from the bigger number. Then repeat the previous step. 
Performing this routine will always cause you to reach a fixed number: 
6174. Then performing the routine on 6174 will always give you 6174 
(7641 - 1467 = 6174). Your program should return the number of times 
this routine must be performed until 6174 is reached. For example: if 
num is 3524 your program should return 3 because of the following steps:
(1) 5432 - 2345 = 3087, (2) 8730 - 0378 = 8352, (3) 8532 - 2358 = 6174. 

'''


def KaprekarsConstant(num):

	count = 0
	while(True):
		count += 1

		num_list = list((str(num)))
		if len(num_list) < 4:
			num_list += ['0']*(4-len(num_list))

		num_list.sort()
		num_asc = int("".join(num_list))
		num_list.sort(reverse=True)
		num_dsc = int("".join(num_list))

		diff = num_dsc - num_asc
		
		if(diff == 6174):
			break
		num = diff
	return count


if __name__ == "__main__":
	print(KaprekarsConstant(1112))