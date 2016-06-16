import random # import the random module

class Human(object):
	def __init__(self, clan=None):
		print "New Human!"

		self.clan = clan
		self.health = 100
		self.strength = 3
		self.intelligence = 3
		self.stealth= 3
	def taunt(self):
		print "You want a piece of me?"

	def attack(self):
		self.taunt()

		#use random to generate a number when we attack
		luck = round(random.random() * 100)
		if(luck > 50):
			if(luck * self.stealth > 150):
				print "Attacking!"
				return True
			else:
				print "Attack failed"
				return False
		else:
			self.health -= self.strength
			print "Attack failed"
			return False