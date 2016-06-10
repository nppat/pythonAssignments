'''
Part I

Given the following list:

students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
Create a program that outputs:

Michael Jordan
John Rosales
Mark Guillen
KB Tonel
'''
''' Part 1 '''
# students = [ 
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def printStudents(a): #define the function with one argument
#     for data in a: # loop through the list
#         print data['first_name'], data['last_name'] #print out the values for first_name and last_name

# printStudents(students) # run the function

'''
Part II

Now, given the following dictionary:

users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
Create a program that prints  the following format (including number of characters in each combined name):

Students
1 - MICHAEL JORDAN - 13
2 - JOHN ROSALES - 11
3 - MARK GUILLEN - 11
4 - KB TONEL - 7
Instructors
1 - MICHAEL CHOI - 11
2 - MARTIN PURYEAR - 13
'''
''' Part 2 '''

users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printUsers(a): #define the function with one argument
    for key in a: #loop through the dictionary
        number = 1 # set the placeholder starting at 1
        print(key)  #print out the key in the dictionary, 'Students' and 'Instructors'
        for value in a[key]:    # Loop through each value (first_name, last_name) in each key
            print number, "-", value['first_name'].upper(), value['last_name'].upper(), "-",(len(value['first_name']) + len(value['last_name']))
            # Print out the placeholder value, the value of each item in the key and the lenght of first and last_name combined 
            number += 1 # add plus one to the placeholder

printUsers(users) #run the function
