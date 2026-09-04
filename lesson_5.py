## CONDITIONAL LOGIC AND DECISION MAKING
#Lesson: Loops and for loops

# A while loop acts like a continuos IF statement. It checks a condition as long as that condition remains TRUE, it keeps running
# the code block underneath over and over again

## A COUNT DOWN USING WHILE LOOP
# Telling python to start counting from 4
#count = 4 # assigning a count to start at 4
# A while loop has a conditional operators working with two values to compare whether count is greater than 0.
# If that statement is true, a colon allows python to print the value of the count
#while count > 0 : #Python will then check if a count is greater than 0, it is greater meaning the condition is True
# Python will then print the value of the count
    #print(count) # we want you to keep printing the value of a count(4)
# We then take the value of a count and minus 1, then we save the results as count meaning we now have a new value of a count
    #count = count - 1 # after count just say count(4) -1 = 3 then 3 is tored in the new variable count
#Meaning count(remainder of 4-1) = count(assigned number(4)) - 1
# NOTE: After saying 4 - 1 the remainder 3 will then replace the old count with the new one (3)
# Then we execute print("Blast Off !!!") after escaping the loop
#print("Blast Off !!!") #then print "Blast Off !!!"
# returned:
# 4 # It started with 4 and checked if 4 was greater than 0, condition was true then returne 3
# 3 # After storing the three it checks again if 3 is greater than 0, condition is true then is returned 2
# 2 # went to check if 2 is greater than 0, condition is true then printed 1
# 1 # went to the loop again to check if 1 is greater than 0 condition was true then goes to 0
# Now when it gets to zero the loop strops and prints out BLAST OFF 
# Blast Off !!!

##FOR LOOP
# If we want to know how many times we want the loop to repeat, we use for loop combined with range funtion
##Task: Building a simple rep counter
#for rep in range (1, 4): # so range tells python to start running from 1 till before 4
    #print(f"This is rep no.{rep}") #rep will be our temporary variable
# the curly braces tell python to go inside the variable rep, look inside of it, tell us the value and replace it in between the {}
# Unlike while loop, in for loop we dont need to subtract anything, python does it automatically
#NOTE: The for loop handles the adding and subtraction of values
# Returned
#This is rep no.1
#This is rep no.2
#This is rep no.3

## COMBINING LOOPS WITH DECISION MAKING
# Write a small script of a game: A GUESSING GAME

#secret_word = "python" # We stored the language python in the variable secret word
# We then say, while that is true it will keep on running until we do something or something changes
#while True:
# The we ask the user to enter the language in the secret word, their response will then be stored under variable guess
 #   guess = input("Guess the programming language we are using: ").lower()
# After storing the language we are going to compare it with the secret word and see if they are the same
 #   if guess == secret_word:
 #if they have inserted the correct secret word python will then print You guessed the correct language
 #       print("You guessed the correct language !!!!")
 #       break # Is one of those reserved key words, we use it to escape the loop.Meaning if the user guesses the correct language
# there's no need to keep on running the loop so break exits the loop
#    else: #Should the user continue printing the incorrect language then python will pring Incorrect guess, try again
#meaning the loop continues
#        print("Incorrect guess, try again !!!!")

# NOTE: We had provided python with multiple incorrect answeres to test the loop until we got to the correct one.
# Then the loop was broken
# Guess the programming language we are using: c++
# Incorrect guess, try again !!!!
# Guess the programming language we are using: java
# Incorrect guess, try again !!!!
# Guess the programming language we are using: c#
# Incorrect guess, try again !!!!
# Guess the programming language we are using: python
# You guessed the correct language !!!!
##END OF LOOP

##SELECTION OF TASKS
# How to select tasks
# Without conditional logic, every program runs the same way every time regardless of input.
# Python checks each condition in order and executes the first block where the condition is True.
# Conditional logics: they let the program to make decisions
# if - Python checks each condition in order and executes the first block where the condition is True.
# elif (else if) - chains multiple conditions
# else - The else block is the fallback, it runs when all other conditions are False
# NOTE: Indentation is not optional, it is how Python knows which code belongs to which condition.

##COMPARISON OPERATORS
# Six comparison operators return True or False: 
# == - (equal to), 
# != (not equal to), 
# > (greater than), 
# < (less than), 
# >= (greater than or equal to), 
# <= (less than or equal to)
# A single = is assignment (age = 22). A double == is comparison (age == 22). 
# NOTE: Confusing these is one of the most common bugs in beginner code.

## LOGICAL OPERATORS
# There are Three logical operators that combine conditions.
# and: both conditions must be True. 
# or: at least one condition must be True. 
# not: inverts the result (True becomes False, False becomes True).
# Example: if age >= 18 and has_id: grants entry only when both conditions are met. 
# NOTE: Logical operators are evaluated after comparison operators, no brackets needed in most cases, but they improve readability.

## THE IN KEYWORD AND TRUTHINESS
# The in keyword checks membership: 
# if ‘admin’ in roles checks whether ‘admin’ is in the roles list. 
# It works on strings too: if ‘@’ in email checks for a valid email format. 
# Python also has a concept of truthiness: 
# empty strings, 
# 0, 
# None, 
# and empty lists are all falsy. This means if username: is a valid check for whether a string is non-empty.

##ADDITIONAL MATERIAL: CONDITIONALS AND BOOLEANS
# The lesson is abount conditionals and how we can control what statements get executred depending on whether certain values
# evaluate to TRUE or FALSE(Booleans)
# lets start with a simple conditinal statement
#if True:
#    print('Conditional was True') 
# Returned: Conditional was True: The print statement will onlt be executed if the condition after our if statement evaluates to true.
#Changed the condition to FALSE
#if False:
#    print('Conditional was True') 
# Nothing was printed out in the terminal.We must out in some code that evaluates to True or False

# 7 comparison operators return True or False: 
# == - (equal to), 
# != (not equal to), 
# > (greater than), 
# < (less than), 
# >= (greater than or equal to), 
# <= (less than or equal to)
# is : Objects identity - Is to check/test if values have the same ID or whether they are the same object in memory
#Example
#language = 'Python'

#if language == 'Python':
#    print('Conditional was True') 
# Returned: Conditional was True: Language is 'Python'
#Example 4 else statements
# We want to execute one portion of our code if our language was equal to Python 
# but another portion of our code if it wasn't Python
#language = 'Python'

#if language == 'Python':
#    print('Language is Python') 
#else: 
#    print("No match")
# Returned: Language is Python: Because when the python evaluated the condition is found that its true
#else is a fall back for when the condion isnt met, see example below:
#Example
#language = 'Python'

#if language != 'Python':
#    print('Language is Python') 
#else: 
 #   print("No match")
#Returned: No match: Because a condition was not mer cause Language is equal to Python but the condition said not equal

# What if we want to check for multiple languages and execute different code for each one that we encountered so this is where 
# an elif(else if) statement comes in.
# Example: checking  if the language  was equal to Python and if it wasn't then we wanted to check if it was equal to Java
# and if it was neither of those then we would just print no match
#language = 'Java'

#if language == 'Python': #If the language is equal to python
#    print('Language is Python') #then execute this code
#elif language == 'Java': # if its not == to python then run the second condition and see if its equal to Java
#     print('Language is Java') #if its equal to Java then run this code
#else: 
#    print("No match") # if no condition was met then print 'NO MATCH'
# Returned: Language is Java because one of two conditions was met
##NOTE:SWITCH STATEMENT - Checks multiple values
# However python doesnt have the switch case statement cause if/elif & else statements are plenty clean enough to do this.
# So if we want to check for another language, all we do is keep on adding elif statements. See exaple below
#Checking fo JavaScript
#language = 'Java'

#if language == 'Python': #If the language is equal to python
#    print('Language is Python') #then execute this code
#elif language == 'Java': # if its not == to python then run the second condition and see if its equal to Java
#     print('Language is Java') #if its equal to Java then run this code
#elif language == 'Java': # if its not == to python then run the second condition and see if its equal to Java
#     print('Language is JavaScript') # Python version of switch case statement
#else: 
#    print("No match")
#Returned : Language is Java

##BOOLEAN OPRERATIONS
# They are as follows
# and
# or
# not

#Example:
#user = 'Admin'
#logged_in = True
# Here we want to execute some code if user is admin and logged in is equal to true
#The achieve this we can use the in keyword, see below
#if user == 'Admin' and logged_in: #if user is == to admin and(keyword) logged in run the code
#     print("Admin Page") # if the condition is met then prnt the string Admin page
#else: #else block
#     print('Bad creds')# if no condition is met then print string Bad cred(credentials)
# Returned: Admin Page: a condition was met, out user is indeed == to admin and logged in i true
# Lets say we change the logged in condition to false
#user = 'Admin'
#logged_in = False

#if user == 'Admin' and logged_in: #if user is == to admin and(keyword) logged in run the code
 #    print("Admin Page") # if the condition is met then prnt the string Admin page
#else: #else block
#     print('Bad creds') 
# Return: Bad creds cause only one condition was true and the AND keyword requres both conditions to be true

## Now we want only one condition to be TRUE we can now use the keyword(OR)
#Example:
#user = 'Admin'
#logged_in = False

#if user == 'Admin' or logged_in: #if user is == to admin and(keyword) logged in run the code
#     print("Admin Page") # if the condition is met then prnt the string Admin page
#else: #else block
#     print('Bad creds')
# Returned: Admin Page: Because only one or the other condition needed to be TRUE
# Our user was indeed == to admin so it didnt matter whether logged in was true or false

## IS NOT: is used to switch a BOOLEAN
# it changes a false to a true and a true to a false
#Example
#user = 'Admin'
#logged_in = False
# Currently our logged in is FALSE so the keyword(NOT) will change it to TRUE
#if not logged_in: #if user is not logged in run the code
 #    print("Please log in") # if the condition is met then print the string Admin page
#else: #else block
#     print('Welcome')
# Returned: Please log in because NOT logged in evaluates to TRUE so it runs what was in our IF STAEMENT 

## HOW TO APPLY THE  'IS" COMPARISON
# is : Objects identity - Is to check/test if values have the same ID or whether they are the same object in memory
#Meaning the two objects may be equal and not be the same object in memory
#Example: creating two different lists
# LIST 1
#a = [1,2,3] #Is list one 
#List 2
#b = [1,2,3] # equal(==) to list two
#print(a == b)
# Returned: True as expected
# LIST 1
a = [1,2,3] #Is list one 
#List 2
b = [1,2,3] # equal(==) to list two
print(a is b)