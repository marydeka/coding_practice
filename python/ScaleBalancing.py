'''
coderbyte: scale balancing

Have the function ScaleBalancing(strArr) read strArr which will contain 
two elements, the first being the two positive integer weights on a balance
 scale (left and right sides) and the second element being a list of available 
 weights as positive integers. Your goal is to determine if you can balance the 
 scale by using the least amount of weights from the list, but using at most 
 only 2 weights. For example: if strArr is ["[5, 9]", "[1, 2, 6, 7]"] then this 
 means there is a balance scale with a weight of 5 on the left side and 9 on the 
 right side. It is in fact possible to balance this scale by adding a 6 to the 
 left side from the list of weights and adding a 2 to the right side. Both scales 
 will now equal 11 and they are perfectly balanced. Your program should return a 
 comma separated string of the weights that were used from the list in ascending 
 order, so for this example your program should return the string 2,6 

There will only ever be one unique solution and the list of available weights 
will not be empty. It is also possible to add two weights to only one side of 
the scale to balance it. If it is not possible to balance the scale then your 
program should return the string not possible. 
'''

#to-do: make code more readable, have the functions call each other

def ScaleBalancing(strArr):
  # smallerWeight = 0;
  # largerWeight = 0

  smallerWeight = findWeights(strArr)[0]
  largerWeight = findWeights(strArr)[1]

  # if addWeightsToOneSide(strArr):
  #   print(addWeightsToOneSide(strArr))

  numbersAddedToOneSide = addWeightsToOneSide(strArr)
  print(numbersAddedToOneSide)
  

def findWeights(strArr):
  
  smallerWeight = 0;
  largerWeight = 0

  if strArr[0][0] < strArr[0][1]:
    smallerWeight = strArr[0][0]
    largerWeight = strArr[0][1]

  else:
    smallerWeight = strArr[0][1]
    largerWeight = strArr[0][0]

  return [smallerWeight, largerWeight]

def addWeightsToOneSide(strArr):
  
  # print(list(range(0, len(strArr[1]))))
  for i in range(0, len(strArr[1])):
    if smallerWeight + strArr[1][i] == largerWeight:
      return i

  # print(list(range(0, len(strArr[1]) -1 )))
  for j in range(0, len(strArr[1]) - 1):
    # print(list(range(j+1, len(strArr[1]))))
    for k in range(j + 1, len(strArr[1])):
      if strArr[1][j] + strArr[1][k] + smallerWeight == largerWeight:
        return [strArr[1][j], strArr[1][k]]

def addWeightToBothSides(strArr):
  for j in range(0, len(strArr[1]) - 1):

    for k in range(j + 1, len(strArr[1])):
      if smallerWeight + strArr[1][j] == largerWeight + strArr[1][k] \
       or smallerWeight + strArr[1][k] == largerWeight + strArr[1][j]:
        return [strArr[1][j], strArr[1][k]]

  return "No way to balance"


if __name__ == "__main__":
  # print(findWeights([[3,4], [1,2,7,7]]))
  # ScaleBalancing([[7, 4], [1, 2, 7, 7]])

  # strArr = [[7, 4], [1, 2, 7, 7]]
  strArr = [[5,9], [1,2,6,7]]
  smallerWeight = findWeights(strArr)[0]
  largerWeight = findWeights(strArr)[1]
  # print(addWeightsToOneSide(strArr))
  print(addWeightToBothSides(strArr))
  