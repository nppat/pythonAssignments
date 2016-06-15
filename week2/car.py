'''
Car

Difficulty Level: BasicEstimated Time: 2-4 hrs
Create a class called  Car. In the__init__(), allow the user to specify
the following attributes: price, speed, fuel, mileage. If the price is greater
than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

Create five different instances of the class Car. In the class have a method
called display_all() that returns all the information about the car as a string.
In your __init__(), call this display_all() method to display information about the
car once the attributes have been defined.

'''
class Car(object): #Create Class Car

	def __init__(self, car_number, price, speed, fuel, mileage): #Define __init__() and set parameters
		self.car_number = car_number
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage

		self.display_all() #Calls display_all() for each instance

	def display_all(self): # define display_all to print out each parameter
		tax = 0
		if(self.price > 10000):	# sets the taxes payed based upon the self.price parameter
			tax = self.price * 0.15
		else:
			tax = self.price * 0.12

		print "Car number:", self.car_number #Prints out paramters
		print "Price - $", self.price 
		print "Speed - ", self.speed
		print "Fuel - ", self.fuel
		print "Mileage - ", self.mileage
		print "Taxes are $",tax,"\n"

# Created 5 different instances
car1 = Car(1,1000,'35mph', '1/4', 5000) 
car2 = Car(2,2000,'45mph', '1/2', 1000)
car3 = Car(3,3000,'55mph', '3/4', 25000)
car4 = Car(4,4000,'65mph', 'Full', 55000)
car5 = Car(5,5000,'75mph', 'Empty', 125000)
