'''
Create a function called 'multiply' that reads each
value in the list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
The function should multiply each value in the list by the second argument.
'''
'''
This is what I came up with first, and it only output [80].  Now I know why.  Each time it would
loop through, it would create a new list, then add to the list each time.  Well that is fine and 
dandy, but it would not hold more than one value, because a new list was created every time.  The
bottom funciton creates the new list first, then runs the loop and add the result to the list, 
saving each iteration of the loop.  
'''
# a = [2,4,10,16]
# def multiply(a,b):
# 	for item in range(len(a)):
# 		i = a[item] * b
# 		newList = []
# 		newList += [i]
# 	return newList

# print multiply(a,5)

a = [2,4,10,16] #list

def multiply(a,b):  #defined a function with two arguments
	newList = []  # create newList to store new values
	for item in range(len(a)): # loop through a 
		newList += [a[item] * b] # add each value of a that is multiplied by b
	return newList #return newList
print multiply(a,5)  #prints out the function to the Terminal