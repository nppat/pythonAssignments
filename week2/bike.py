'''
Bike

Create a new class called  Bike with the following properties/attributes:

price
max_speed
miles
Create 3 instances of the Bike class.

Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.

Add the following functions to this class:

displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().

What would you do to prevent the instance from having negative miles?
'''

class Bike(object): #Create the class
	def __init__(self, bike_name, price, max_speed, miles = 0): #Initialize and add attributes

		self.bike_name= bike_name
		self.price = price
		self.max_speed = max_speed
		self.miles = miles

	def displayInfo(self):
		print "Bike # ",self.bike_name," Price - ",self.price," Max Speed - ",self.max_speed," Miles - ",self.miles,"\n"
		return self # Returns its own instance, saves me from a lot of extra typing

	def ride(self):
		self.miles += 10 #Adds 10 miles to miles
		print "Riding bike # ",self.bike_name," New mileage - ",self.miles
		return self

	def reverse(self):
		if self.miles >= 5: #Checks to see if mileage is above 5 miles
			self.miles -= 5
			print "Reversing bike # ",self.bike_name," New mileage - ",self.miles
		return self

''' Create 3 instances '''
bike1 = Bike("1",20, '25mph',)
bike2 = Bike("2",10, '20mph', 6)
bike3 = Bike("3",15, '18mph', 8)

# ''' Run the methods as described in the instructions '''
# bike1.ride(),bike1.ride(),bike1.ride()
# bike2.ride(),bike2.ride()
# bike1.reverse(),bike1.reverse()
# bike2.reverse(),bike2.reverse()
# bike3.reverse(),bike3.reverse(),bike3.reverse()
# bike1.displayInfo()
# bike2.displayInfo()
# bike3.displayInfo()

''' Instances are shown calling all the methods, but using return self, saving a lot of extra typing'''
bike1.ride().ride().ride().reverse().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
