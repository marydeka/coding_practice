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

#still working on this. For instance, I have to figure out how to calculate if the pieces 
#are diagonal from each other. Debugging as I go along. 

def EightQueens(strArr): 

    # code goes here 
    # width = 8
    # height = 8
    array = []
    for i in range(0, 8):
      num = strArr[i][1] 
      array.append(num)
    	for j in range(0, len(array)):
    		if num == array[j]:
    			return True
  			else:
  				return False
      # print(array)


        # if num == strArr[i][j]:
        #     return strArr[i]
        # else: 
        # 	return True
        

    
if __name__ == "__main__":
	print(EightQueens(["(2,1)", "(5,3)", "(6,3)", "(8,4)", "(3,4)", "(1,8)", "(7,7)", "(5,8)"]))  