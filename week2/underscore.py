'''
Underscore

Implement the 5 methods using delegating callbacks.  Modify the 5 methods
to take in an array and a callback.

'''

class Underscore(object): # create class Underscore
	def map(self, a, callback): # define method map with 3 arguments
		newList = [] # create a new list to store what is calledback in
		for item in a:	# loop through a
			newList.append(callback(item))#for each item in a, append to newList the new values that are created w/ the lambda and calledback
		return newList # return the new list

	# def reduce(self,x,y,callback):
		




	def find(self, a , callback): # find is similiar to filter(), but returns the first value to pass the truth test
		for item in a: # loops through a
			if callback(item) == True: # checks item against truth test
				return item # returns first item that passes truth test

	def filter(self, a , callback): # define method filter() 
		myList = []	# create a new list to store new values
		for item in a: # loop through a
			if callback(item) == True: # if the callback for the item is true,
				myList.append(item) # add the new item to the new list myList
		return myList # return the new list, myList

	def reject(self, a , callback): # returns a list of the values that that did not pass the truth test
		myList = [] # create new list to store new values in
		for item in a:	# loop throuh a
			if callback(item) == False: # check each item to see if it fails truth test
				myList.append(item) # add those that fail truth test to myList
		return myList # return the new list

''' Create instance '''
_ = Underscore()

''' Create List to test '''
test = [1,2,3,4,5,6]

''' _.map test '''
squared = _.map(test, lambda x: x ** 2)
print "########### Map ###############"
print "Square each number"
print test
print squared, "\n"

''' _.reduce test '''
''' _.find test '''
findOdd = _.find(test, lambda x: x % 3)
print "########### Find ###############"
print "Will find and return first odd number"
print test
print findOdd, "\n"
''' _.filter test '''
evens = _.filter(test, lambda x: x % 2 == 0)
print "########### Filter ###############"
print "Will find and filter out all odd numbers, printing only the evens"
print test
print evens,"\n"
''' _.reject test '''
rejectEvens = _.reject(test, lambda x: x % 2 == 0)
print "########### Reject ###############"
print "Checks each item to see if it is an even number, returns all odd numbers"
print test
print rejectEvens