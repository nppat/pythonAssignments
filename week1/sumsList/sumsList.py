# a = [1,2,4,10,255,3]
# count = 0
# while count < len(a):
# 	count += a[i]
# print count


'''Using sums()'''
# a = [1,2,4,10,255,3]
# print sum(a)

'''
While trying to go through the loop and add to the count, I couldn't figure out to
add the index value, while searching on Google for an example, I found sum(). Using this
sum() utiziled two lines of code and worked the same to get the sum of the list
'''

''' Not using sums() '''
a = [1,2,3,4,5]
sums = 0
for item in a:
	sums += item
print sums