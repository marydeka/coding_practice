#coderbyte: reverse a string

def FirstReverse(str):
	str_reverse = " "

	for i in str:
		str_reverse = i + str_reverse

	return str_reverse

print FirstReverse(raw_input())
