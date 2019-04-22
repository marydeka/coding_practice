''' 
#coderbyte: Have the function PentagonalNumber(num) read num which will be a positive integer 
and determine how many dots exist in a pentagonal shape around a center dot on the Nth iteration.
or example, in the image below you can see that on the first iteration there is only a single 
dot, on the second iteration there are 6 dots, on the third there are 16 dots, and 
on the fourth there are 31 dots. 
'''

def PentagonalNumber(num): 

    # code goes here
    if num == 1:
        return 1
    else: 
        return PentagonalNumber(num - 1) + 5 * (num -1)
  
    
if __name__ == "__main__":
	print(PentagonalNumber(5))

