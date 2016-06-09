'''
Part 1
Create a function called  draw_stars() that takes a list of numbers and prints out  *.

For example:

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x) should print the following in when invoked:

**** 
****** 
* 
*** 
***** 
******* 
*************************


Part 2
Modify the function above. Allow a list containing integers and strings to be passed to the  draw_stars() function.
When a string is passed, instead of  displaying *, display the first letter of the string according to the example below.
You may use the .lower() string method for this part.

For example:

 x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x) should print the following in the terminal:

**** 
ttt 
* 
mmmmmmm 
***** 
******* 
jjjjjjjjjjj
'''
''' Part 1 '''
# x = [4, 6, 1, 3, 5, 7, 25]

# def draw_stars(a):  # define the function
# 	for item in a:	# loop through each item in the list, which is passed to the function via (a)
# 		print('*' * item)  #print stars that equal the value of the item in the list

# draw_stars(x)


''' Part 2 '''
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(a):
	for item in a:
		if (type(item) == int):
			print ('*' * item)
		elif (type(item) == str):
			print (item[0].lower() * len(item))

draw_stars(x)














