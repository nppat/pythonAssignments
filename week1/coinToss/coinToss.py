'''
You're going to create a program that simulates tossing a coin 5,000 times. Your program should display how many times the head/tail appears.

Knowns:
	coin is simulated to be tossed 5,000 times
	have to use random number generator
	0 could be tails
	1 could be heads
	use round() to round up or down

Unknowns:
'''
'''
import random

def coinToss():
	heads = 0 #sets the var to 0 
	tails = 0 #sets the var to 0 
	count = 0 #sets the var to 0 

	for count in range(0,5000): #loops through the range from 0 to 5000
		r = random.randint(0,1) # gets a random number of 0 or 1
		if (r == 0): # if r is 0, then it is a tails and the counter and tails var are +1 and the printout ensues
			tails += 1
			count += 1
			print 'Attempt',count,'is heads.  The totals are ',heads,'heads and',tails,'tails.'
		else:  # if r is 1, then it is a heads and the counter and heads var are +1 and the printout ensues
			heads += 1
			count += 1
			print 'Attempt',count,'is tails.  The totals are ',heads,'heads and',tails,'tails.'
	print "There were",heads,"heads and ",tails,"tails flipped."
	return;

coinToss()
'''


'''
This block of code uses a random.random() that is then sent to variable x and is rounded either up or down.
The basis of the rest of the code is the same as that above.  I wanted to make sure I could use both ways, as I 
had some problems getting the random.random() method to work using the round() function.

Both work.
'''
import random

def coinToss():
	tails = 0
	heads = 0
	count = 0

	for count in range(0,5000):
		r = random.random()
		x = round(r)
		if(x == 0):
			count += 1
			tails += 1
			print 'Attempt',count,'is heads.  The totals are ',heads,'heads and',tails,'tails.'
		else:
			count += 1
			heads += 1
			print 'Attempt',count,'is tails.  The totals are ',heads,'heads and',tails,'tails.'
	print "Attempts: ",count,"Heads: ",heads,"Tails: ",tails
	return;

coinToss()