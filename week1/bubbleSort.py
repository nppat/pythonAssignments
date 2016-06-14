'''
Bubble Sort
'''

numbers = [5,3,4,1]

for number in range(len(numbers)):
	for i in range(number):
		if numbers[i] > numbers[i + 1]:
			temp = numbers[i]
			numbers[i] = numbers[i + 1]
			numbers[i + 1] = temp
print numbers