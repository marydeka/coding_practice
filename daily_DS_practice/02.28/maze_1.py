'''
Iteration 1

Given input that represents a maze, write a program that finds a valid
solution to the maze by outputting directional instructions from
the start marker to the finish marker.

Maze characters:
S start
F finish
+ open space
@ barrier

The first line of the input is an integer value N, such that 1 <= N <= 1000,
for the amount of rows in the maze.

Output should be a string of commands to move through the maze from start to finish. 

D=down, R=right, L=left, U=up

Sample Input #1:  output should be DRRRD
3
S@@@
++++
@@@F

'''

maze = [["S@@@"], ["++++"], ["@@@F"]]

print(maze[0][0])

print(len(maze))
print(len(maze[1]))

