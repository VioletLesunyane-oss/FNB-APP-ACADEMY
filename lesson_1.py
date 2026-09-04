# Making the computer speak (Hashtag is for writing comment, on SQL is --)
# print is for anouncing what we want to show
# always use double quotes (single quotes can also be used), so double quotes instriucts python not to write the code but to print exactly what's within the
# double quotes.
#print("hello world!") hello world is a string

# Storing data inside a variable
#name = "Violet" # Violet is a name that we stored in a variable called "name"
#print(name) # we then bring the name(variable/container) to the terminal.
# So here we don't use double quotes cause they are already on the mane "Violet"
#print("name") # so in this case, the double quotes will instruct python to print a word "name" which is a "string/str"

# Making the code interactive
# name - a variable(strore/container)
# Violet - is a value that is stored in the container called name
# = - is an operator that assigns the value to the container, so it assigns the value VIOLET to the container   
# input - Its a function that allows the user to input data.
#Note: after running the code below, it will first show "Enter your name:" first, 
# then is will wait for the user to enter their name on the terminal, press enter and then it will print "Greetings, name",
#name which is Violet so it will bw Greetings, Violet
# it will not run unless the name or value is entered
# "F" tells python the formated string to start printing Greetings and then go into the {} look at what is 
# written inside and print it out, in this case it will print out the name that was enteres by the user.
#name = input("Enter your name:")
#print(f"Greetings, {name}")

#Youtube task with Mosh
#name = "John Smith"
#age = 20
#new_patient = True
#print(name, age, new_patient)

# input - reads a value from the terminal and stores it in a variable, so the user can input whichever value they want. In this 
# its a name
#input("What is your name? ") # This returns the value "What is your name?" and then waits for the user to input whichever name
# name they choose eg, Violet and then it stores that name somewhere in the memory but the user must then store it in a variable,
# See below
#name = input("What is your name? ") # Here we are puting the value in a variable/container called name.
#print("Hello " + name) #This is what we call string concatination, its when we join 2 strings together. 

#Converting a variabble fron one data type to another 
#birth_year = input("Enter your birth year: ") # This will return a string value, so if we want to do same math with it, 
# we convert it to an integer using int() function.
#age = 2026 - int(birth_year)
#print(age)
# Within the window below the code 1st retuned "Enter your birth year" and then i typed my birth year and it returned my correct age.
# so by adding int() function we converted the string birth year in to a number when i typed it below.
#That's when i was able to subtract my birth year from 2026.

# float() Decimal Number (39.0)
# int() Numbers (39)  
# bool() True/False 
#str() Letters (Violet)
# So these are the built-in functions for converting a variable from one data type to another.

#Example
#first = input("First: ")
#first = "10"
#second = input("Second: ")
#second = "20"
#sum = int(first) + int(second)
#print(sum)
#Output = 30

# So if you i want to to add a whole number with a decimal number,i will then use float() function and not int()function
#e.g.
#first = input("First: ")
#first = "10"
#second = input("Second: ")
#second = "20.1"
#sum = float(first) + float(second)
#print(sum)
#Output = 30.1

#ALTERNATIVELY, we can do it this way
# Beacause doesnt know how to add a float with an int so we will do it this way
#first = input("First: ")
#first = "10"
#second = input("Second: ")
#second = "20.1"
#sum = float(first) + float(second)
#print("Sum: " + str(sum))

#ANOTHER ALTERNATIVE METHOD
#first = float(input("First: "))
#second = float(input("Second: "))
#sum = first + second
#print("Sum: " + str(sum))
#Output = 30.1

#Converting lowercase to uppercase 
#Another Example
#course = 'Python for beginners'
#course is a variable/container and 'Python for beginners' is an object
#when one types course. it will show all the methods that can be used with the object which are specific to the object.
# they are also called methods of the object.When a function is associated with an object, we call it a method.
# Now if we use a method called upper() which is a method that converts the string to uppercase,
#E.g.
#print(course.upper()) # This will return PYTHON FOR BEGINNERS
#print(course.lower()) # This will return python for beginners
#print(course) #This will return the original string which is Python for beginners
#print(course.find('y')) # This will return 1, which is the index of the letter y in the string because Python counts the
#index from 0, T=O Y=1 T=2 H=3 O=4 and N=5
#Python is case sensitive, so if we put a Y it will return -1
#print(course.replace('for','4')) #This will return Python 4 beginners, so it replaces the word for with 4
#Note:In python strings can't be changed, so when we replace it creates a new string but original string remains the same.
#print('Python' in course) #This will return True (a boolean) because the word Python is in the string course, 
#so it checks if the word Python is in the string course and return True or false.

#ARITHMETIC OPERATORS
#These are the same arithmetisa that we have in math.
#print(10 + 3) #addition output = 13
#print(10 - 3) #substraction output = 7
#print(10 * 3) #multiplication output = 30
#print(9 / 3) #division output = 3.0 it returns a decimal
#print(3 // 3) #integer division output = 1 we use // to get a whole number (integer)
#print(9 % 3) #modulo output = 0 it returns the remainder of the division of 9 by 3
#print(10 ** 3) #exponentiation output 1000 this is basically 10 to the power of 3

#AUGMENTED ASSIGNMENT OPERATOR
#Lets say we have a variable called x = 10 now we increament the value of x by 3
x = 10
x = x + 3
print(x)
