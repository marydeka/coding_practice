'''
coderbyte:
Have the function EightQueens(strArr) read strArr which will be an array consisting 
of the locations of eight Queens on a standard 8x8 chess board with no other pieces 
on the board. The structure of strArr will be the following: ["(x,y)", "(x,y)", ...] 
where (x,y) represents the position of the current queen on the chessboard (x and y will both 
range from 1 to 8 where 1,1 is the bottom-left of the chessboard and 8,8 is the top-right). 
Your program should determine if all of the queens are placed in such a way where none of them 
are attacking each other. If this is true for the given input, return the string true otherwise
 eturn the first queen in the list that is attacking another piece in the same format it was 
provided. 

For example: if strArr is ["(2,1)", "(4,2)", "(6,3)", "(8,4)", "(3,5)", "(1,6)", "(7,7)", "(5,8)"] then your program should return the string true. 

'''

#can't figure out what I'm still getting tabs and indentation error on line 34

def EightQueens(strArr): 

 
  array = []
  for i in strArr:
    array.append([int(i[1]), int(i[3])])
  for j in range(0, len(array) - 1):
  	for k in range(j + 1, len(array)):
  		x1 = array[j][0]
  		x2 = array[k][0]
  		y1 = array[j][1]
  		y2 = array[k][1]
  		if x1 == x2 or y1 == y2 or x1 - x2 == y1 - y2:
  			return "(" + str(x1) + "," + str(y1) + ")"
	
	return "true"
		
			
 

    
if __name__ == "__main__":
	print(EightQueens(["(2,1)", "(5,3)", "(6,3)", "(8,4)", "(3,4)", "(1,8)", "(7,7)", "(5,8)"]))  