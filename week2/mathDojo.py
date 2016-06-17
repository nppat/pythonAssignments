'''
MathDojo

HINT: To do this exercise, you will probably have to use 'return self'.
If the method returns itself (an instance of itself), we can chain methods.

PART I
Create a Python class called MathDojo that has the methods  add and subtract.
Have these 2 functions take at least 1 parameter. 

Then create a new instance called md. It should be able to do the following task:

MathDojo().add(2).add(2, 5).subtract(3, 2).result
which should perform 0+2+(2+5)-(3+2) and return 4.

PART II
Modify MathDojo to take at least one integer(s) and/or list(s) as a parameter
with as many value passed in the list. It should now be able to perform the following tasks:

MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
 should do 0+1+3+4+(3+5+7+8)+(2+4.3+1.25)-2-(2+3)-(1.1+2.3) and return its result.

PART III
Make any needed changes in MathDojo in order to support tuples of values in addition to lists and singletons.
'''

class MathDojo(object): # create class MathDojo
	def __init__(self):	# initiate attributes
		print "I am a math"
		self.sum = 0

	def add(self,*number): #define add() with * indicating multiple arguments can be passed
		for num in number: # loop through number
			if(isinstance(num, list)): # check instance for type, in this case a list
				for item in num: # loop through each item in the list
					self.sum = self.sum + item # add each item to self.sum
			elif isinstance(num, tuple): #check instance for type tuple
				for item in num:
					self.sum = self.sum +item
			else: # if instance is not type = list or tuple, 
				self.sum = self.sum + num # add each num in number to self.sum
		return self # allow chaining

	def subtract(self,*number): #The same rules apply to this method as well
		for num in number:
			if(isinstance(num, list)):
				for item in num:
					self.sum = self.sum - item
			elif isinstance(num, tuple): #check instance for type tuple
				for item in num:
					self.sum = self.sum - item
			else:
				self.sum = self.sum - num
		return self

	def result(self): # define method result, which takes self.sum and prints it
		print self.sum
		return self

''' Create instance '''
md = MathDojo()

''' Run the program with the end result being
I am a math
28.15
56.3
'''
md.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()
md.add([1],3,4).add([3, (5), 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()
