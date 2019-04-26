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

#still working on debugging this, since it doesn't work for all cases

import math

def MaximalSquare(strArr):

	maxCount = 0
	count = 0
	square = False
	

	for i in range(0, len(strArr)):
		for j in range(0, len(strArr[0])):
			if strArr[i][j] == '1' :
				square = True
				maxCount = 1
				if checkNeighbors(strArr, i, j):
					count = math.pow(i + 1, 2)
					if count > maxCount:
						maxCount = count

# def checkNeighbors(strArr, i, j):
# 	increment = False
# 	if strArr[i + 1][j] == '1' and strArr[i][j +1] == '1' and strArr[i + 1][j + 1] == '1' :
# 		increment = True
# 	return increment

def checkNeighbors(strArr, i, j):

	for i in range(i, len(strArr) - i):
		for j in range(j, len(strArr[0]) - j):
			for n in range()
			if strArr[]
			if strArr[i][j] != '1':
				break
			return True








			# if strArr[i][j] == '1' and strArr[i][j + 1] == '1' \
			# and strArr[i + 1][j] == '1' and strArr[i + 1][j + 1] == '1' :

			# 	count = 4
			# 	while i + n <= len(strArr) and j + n <= len(strArr[0]):
			# 		if strArr[i][i + n] == '1' and strArr[i + n][i] == '1' :
			# 			count = math.pow(n + 1, 2)
			# 		n += n

			# if count == 0 and strArr[i][j] == '1' :
			# 	return 1
	

if __name__ == "__main__":
	print(MaximalSquare(["10100", "10111", "11111", "10010"]))