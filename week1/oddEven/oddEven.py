'''
Create a function that counts from 1 to 2000. As it loops through each number,
have your program generate the number and specify whether it's an odd or even number.
'''
for count in range(1,2001):
	if (count%2 == 0):
		print 'Number is',count,'.  This is an even number.'
	else:
		(count%2 == 1)
		print 'Number is',count,'.  This is an odd number.'