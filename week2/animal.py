'''
Create a class called Animal with the following attributes: name, and health.
Give the animal following three methods: walk, run, and displayHealth. Give a new animal a
health of 100 when it gets created. When a walk() method is invoked, have the health decrease by 1.
When a run() method is involved, have the health decrease by 5. When a displayHealth() method is invoked,
display on screen the name of the Animal and the health.

Create an instance of the animal called 'animal' and have this animal walk three times, run twice, and have it display its health.

Now, create another class called Dog that inherits everything that the Animal does and have, but
1) have the default health be 150 and 
2) add a new method called pet, which when invoked,
	increase the health by 5. Have the Dog walk() three times,
	run() twice, pet() once, and have it displayHealth().

Now, create another class called Dragon that also inherits everything from Animal, but
1) have the default health be 170 and
2) add a new method called fly, which when invoked, 
	decreased the health by 10. Have the Dragon walk() three times, run() twice, fly() twice,
	and have it displayHealth(). When the Dragon's displayHealth function is called, have it say 'this is a dragon!'
	before it displays the default information (by calling the parent's displayHealth function).

Now for the first instance of the animal (instance called 'animal'), try calling fly() or pet() and make sure this doesn't work.  (-:
'''

class Animal(object): # create class Aninmal
	def __init__(self, name): # set the attributes each instance should have
		self.name = name
		self.health = 100	#health is not something the user can set

	def walk(self): # define method walk()
		self.health -= 1 # when called, subtract 1 from health
		return self # method is able to return itself

	def run(self): #define method run()
		self.health -= 5 #subtract 5 from health when ran
		return self #allow chaining by returning self

	def displayHealth(self): #define method displayHealth()
		print self.name, self.health #print out the instance called name and health
		return self #allow chaining

class Dog(Animal): #create class Dog that inherits off of class Animal
	def __init__(self,name): #set the attributes for class Dog
		super(Dog,self).__init__(name) #use super to inherit attributes from Animal by way of .__init__()
		self.health = 150 #class Dog health starts out at 150

	def pet(self): #define method pet()
		self.health += 5 #increase health by 5
		return self # allow chaining

class Dragon(Animal): #create class Dragon inheriting from class Animal
	def __init__(self,name): #set up attributes
		super(Dragon, self).__init__(name)  #use super to inherit attributes from Animal by way of .__init__()
		self.health = 170 # class Dragon health starts at 170

	def fly(self): #define method fly()
		self.health -= 10 # decrease health by 10
		return self # allow chaining

	def displayHealth(self): #define displayHealth()
		print "This is a dragon" #print out message
		super(Dragon,self).displayHealth() #use super to inherit displayHealth() from Animal by .displayHealth()

'''Create instances'''
animal = Animal('Abner')
dog = Dog("Abe")
dragon = Dragon("Dragon")

'''Run program using all three instances'''
animal.walk().walk().walk().run().run().displayHealth()
dog.walk().walk().walk().run().run().pet().displayHealth()
dragon.walk().walk().walk().run().run().displayHealth()

''' Test to see if calling fly() or pet() with instance of animal works, and it does not, which is what is expected'''
# animal.fly()
# animal.pet()




