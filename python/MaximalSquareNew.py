'''
coderbyte: Maximal Square

Have the function MaximalSquare(strArr) take the strArr parameter being passed 
which will be a 2D matrix of 0 and 1's, and determine the area of the largest 
square submatrix that contains all 1's. A square submatrix is one of equal width 
and height, and your program should return the area of the largest submatrix that 
contains only 1's. For example: if strArr is ["10100", "10111", "11111", "10010"] 
then this looks like the following matrix: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0 

For the input above, you can see the bolded 1's create the largest square submatrix 
of size 2x2, so your program should return the area which is 4. You can assume the 
input will not be empty. 
'''


def areaOfSquare(arr): 
	maxSide = 0

	for i in range(0, len(arr)):
		for j in range(0, len(arr[0])):
			if arr[i][j] == 1:
				side = lengthOfSide(arr, i, j)
				if side > maxSide:
					maxSide = side
	
	return maxSide*maxSide


def lengthOfSide(arr, i, j):
	maxLength = len(arr) - i
	maxWidth = len(arr[0]) - j

	maxSide = 1

	if maxLength <= maxWidth:
		maxSide = maxLength
	else:
		maxSide = maxWidth

	side = 1

	for sideToTest in range(1, maxSide + 1):

		if(isItAllOnes(arr,i,j,sideToTest)):
			side = sideToTest
		else:
			side = sideToTest - 1
			return side
	# print("side = " + str(side))
	return side


def isItAllOnes(arr, i,j,s):
	ans = True
	for m in range(i, i + s):
		for n in range(j, j + s):
			# print("m, n = " + str((m,n)))
			if arr[m][n] == 0:
				# print("m, n after found 0 = " + str((m,n)))
				ans = False
				break

	return ans


if __name__ == "__main__":
	arr = [[1,0,1,0,0], [1,0,1,1,1], [1,1,1,1,1], [1,0,0,1,0]]
	arr = [[0,0,0,0,1,0], [0,1,1,1,1,0], [0,1,1,1,1,1], [0,1,1,1,1,1], [0,1,1,1,1,0], [0,0,0,0,0,0]]

	# # Testing isItAllOnes
	# print(isItAllOnes(arr, 0,0,2)) # --> False
	# print(isItAllOnes(arr, 2,0,2)) # --> False
	# # print(isItAllOnes(arr, 2,0,3)) # --> Error
	# print(isItAllOnes(arr, 1,2,2)) # --> True
	# print(isItAllOnes(arr, 2,4,2)) # --> Error
	

	# Testing lengthOfSide
	# print(lengthOfSide(arr, 1,2)) # 2
	# print(lengthOfSide(arr, 0,0)) # 1
	# print(lengthOfSide(arr, 0,1)) # 0
	# print(lengthOfSide(arr, 3,4)) # 0
	# print(lengthOfSide(arr, 3,3)) # 1


	print(areaOfSquare(arr))

