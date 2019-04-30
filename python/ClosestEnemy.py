
'''
Have the function ClosestEnemyII(strArr) read the matrix of numbers stored in strArr which 
will be a 2D matrix that contains only the integers 1, 0, or 2. Then from the position in the
 matrix where a 1 is, return the number of spaces either left, right, down, or up you must move 
 to reach an enemy which is represented by a 2. You are able to wrap around one side of the matrix 
 to the other as well. For example: if strArr is ["0000", "1000", "0002", "0002"] then this looks 
 like the following: 

0 0 0 0
1 0 0 0
0 0 0 2
0 0 0 2 

For this input your program should return 2 because the closest enemy (2) is 2 spaces away from the 1 
by moving left to wrap to the other side and then moving down once. The array will contain any 
number of 0's and 2's, but only a single 1. It may not contain any 2's at all as well, where in that 
case your program should return a 0. 
'''

def findOnes(matrix):
  for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
      if matrix[i][j] == '1':
        pos1 = [i, j]
        return pos1

def findTwos(matrix):
  for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
      if matrix[i][j] == '2':
        pos2 = [i, j]
        return pos2

  return "No two found"

#to-do: figure out how to wrap around if that would give shortest distance

def shortestDistance(matrix, pos1, pos2):
  #set shortestDistance at first to the largest possible difference
  shortestDistance = (len(matrix) - 1) + (len(matrix[0]) - 1)

  if pos1[0] == pos2[0]:
    shortestDistance = abs(pos1[1] - pos2[1])

  if pos1[1] == pos2[1]:
    shortestDistance = abs(pos1[0] - pos2[0])

  if pos1[0] != pos2[0] and pos1[1] != pos2[1]:
    shortestDistance = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

  return shortestDistance


if __name__ == "__main__":
  matrix = ["0000", "1000", "0002", "0000"]
  pos1 = findOnes(matrix)
  pos2 = findTwos(matrix)
  print("pos1: " + str(pos1))
  print("pos2: " + str(pos2))
  print(shortestDistance(matrix, pos1, pos2))