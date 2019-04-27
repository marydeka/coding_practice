'''
Have the function QuestionsMarks(str) take the str string parameter, which 
will contain single digit numbers, letters, and question marks, and check 
if there are exactly 3 question marks between every pair of two numbers 
that add up to 10. If so, then your program should return the string true, 
otherwise it should return the string false. If there aren't any two numbers 
that add up to 10 in the string, then your program should return false as well. 

For example: if str is "arrb6???4xxbl5???eee5" then your program should return
true because there are exactly 3 question marks between 6 and 4, and 3 question 
marks between 5 and 5 at the end of the string. 
'''



def QuestionMarks(s):
	strArr = list(s)
	result = False

	print("outer range: " + str(list(range(0, len(strArr) - 1))))
	for i in range(0, len(strArr) - 1):
		print("i: " + str(i))

		if strArr[i].isdigit():
			print("inner range: " + str(list(range(i + 1, len(strArr)))))
			for j in range(i + 1, len(strArr)): 
				print("	j: " + str(j))
				

				if strArr[j].isdigit():
					print("		two numbers found")

					if int(strArr[i]) + int(strArr[j]) == 10:
						print("			numbers sum to ten")
						if(numPunctuation(strArr, i, j)):
							print("				true")
							result = True
						else:
							return False
	return result

def QuestionMarks2(s):
	strArr = list(s)
	result = False

	lastSeenNumber = 0
	lastNumberIndex = 0

#to-do: figure out logic for lastSeenNumber and lastNumberIndex

	print(list(range(0, len(strArr))))

	for i in range(0, len(strArr)):
		if strArr[i].isdigit():

			# lastSeenNumber = strArr[i]
			# lastNumberIndex = i

			# print("	lastSeenNumber: " + str(lastSeenNumber))
			# print(" lastNumberIndex " + str(lastNumberIndex))

			if int(strArr[i]) + int(lastSeenNumber) == 10:
				if(numPunctuation(strArr, lastNumberIndex, i)):
					result = True
				else: 
					result = False

			lastSeenNumber = strArr[i]
			lastNumberIndex = i

	return result


def numPunctuation(strArr, a, b):
	arr = list(strArr)
	# print(arr)
	numPunctuation = 0
	for i in range(a + 1, b):
		if arr[i] == '?':
			numPunctuation += 1
	# print(numPunctuation)
	if numPunctuation == 3:
		return True
	else:
		return False
            

if __name__ == "__main__":
	print(QuestionMarks2("rb6??4")) 
	print(QuestionMarks2("4???6???4"))
	print(QuestionMarks("4???6???4"))

	#Testing numPunctuation
	# if (numPunctuation("1??9", 0, 3)):
	# 	print("is true")
	# else:
	# 	print("is false")

