'''
Create a program that prompts the user ten times for a test score between 60 and 100.
Each time a score is generated, your program should display what is the grade of that score.

Here is the grade table:

Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A
'''

scores = [] #holds the values that are going to be inputed by the user

def printGrades(scores): #function takes the grade and sorts them to tell the user where they stand
	for grade in scores: #each grade is in the scores list
		if grade  < 70:
			print 'Your score is ',grade, 'and your letter grade is a D.'
		elif grade < 80:
			print 'Your score is ',grade, 'and your letter grade is a C.'
		elif grade < 90:
			print 'Your score is ',grade, 'and your letter grade is a B.'
		else:
			print 'Your score is ',grade, 'and your letter grade is an A.'
	average = sum(scores)/len(scores) # takes the inputs and averages them
	print 'Your average grade is',average,'.' #prints the average for the user to see

def getScores(): #this functions collects the input from the user
	while (len(scores) < 10): #collects 10 grades from user
		try:
			userinput = float(raw_input("Please enter a grade between 60 and 100: ")) #accepts floats so decimals can be included
		except ValueError: # requires user to input numbers
			print("Please provide a number.")
		else:
			if not 60 <= userinput <= 100: #requires the input to be between 60 and 100
				print("Please provide a number between 60 and 100.")
			else:
				scores.append(userinput) #takes user input and appends it into the scores list
				print("Score added.")
	printGrades(scores) 

getScores() #runs function