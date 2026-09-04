##STORAGE AND ACCESS
# Now we are giving our progrmmes a BRAIN
# Every script thus far has executed sequentially from top to bottom running exact same line everytime
# Howeve, real software doesn't work like that, it need to adapt and make decisions based on what the user does
# I will now be learning about control flow usin if, elif and else statement to let out code to choose its own path

#For better understanding, i will be tackling the lesson like a robot
# for instance, If its green then GO
# If yellow, SLOW DOWN
# If its anything else which is tyhe colour red in this regard the STOP
# This is how the if statement works with code

# Activity: Create a security checker for people of a certain age who want to enter an establishment
# Build a basic if/else statement script
# We are asking the user to enter his age
#age = int(input("Enter your age: ")) # because age is a whole number we there for use an int which automatically converts a string age to a whole number
#We then programmed our system to give access to people who are 18 and above
#if age >= 18: # if a person is 18 and above (also know as comparison statement)
# The dot notaion (:) after 18 gives python a green light that if the statement is TRUE then print Access grantes 
 #   print("Access granted !!!") # then grant them access (known as a comparison operator)
#else:# else if they are below the age of 18. Else can also be refered as a fall back statement (If not this then that)
# And if its not TRUE then print Access denied
  #  print("Access denied !!!") # then deny them access
# NOTE: the if statement uses an or >or= the return True or False. So we need one of the two conditions be met (TRUE)
# meaning we want the age to be exactly 18 or above 18
# Note: the space before print must always be there, it called indentation.Python must know which line to run 

##OUTPUT
#Enter your age: 15
#Access denied !!!
#On the terminal we entered the age 15 which was the stored as an int in a variable and Access was denied cause 15 is not either >nor= 18

# i then entered 23 in the terminal
#OUTPUT
#Enter your age: 23
#Access granted !!!
#WHY: because a condition was met, 23 is grater than 18 but to equal to 18 hence Access granted was returned

#Exercise 2
#age = int(input("Enter your age: "))
#section_pass = input("Do you have a VIP ticket ? (yes/no) ").lower()
#if age >= 18 and section_pass == "yes":  #Both statement must meet a condition
 #   print("Access grated to the VIP section")
#elif age >= 18: # elif is else if. You can put as many elifs as you want to check for multiple condition
# as long as at the end we will be left with a conclusion else
#    print("Access granted to the general section !!!") 
#else:
#    print("Access denied !!!") 
#OUTPUT: 
#Enter your age: 17 (entered 17 in the terminal)
#Do you have a VIP ticket ? (yes/no) yes (entered yes)
#Access denied !!! # access was denied cause because a condition was not met which is >=18 even if i have a VIP ticket

# Trying with age 20
#OUTPUT
#Enter your age: 20
#Do you have a VIP ticket ? (yes/no) yes
#Access grated to the VIP section
#Same process was followed

# Trying with age 23 but no VIP ticket
#OUTPUT
#Enter your age: 23
#Do you have a VIP ticket ? (yes/no) no
#Access granted to the general section !!!
# As i have mentioned above that both conditions must be met in the if age >= 18 and section_pass == "yes":statement 
# in order to get access
# if both conditions are not met, access will be granted but in the general section and not VIP 
# cause they don't have the VIP ticket, even though they are the right age

## STORAGE AND ACCESS
# How do we srore and access data?
# Through:
#1. Lists
# A list is an ordered, mutable collection of values stored in a single variable.
# list is created with square brackets []: students = ['Amara', 'Sipho', 'Lerato'].
# In a list we access items by indexing, basically it assigns a number to a value. 'Amara':[0], Sipho[1] so on and so forth.
# Negative indexes count from the end meaning in this regard 'Lerato' will be [-1].
# Key list methods: .append(item) adds to the end; .insert(index, item) inserts a position; .remove(item) removes by value;
# .pop(index) removes by index and returns the item; .len(list) returns the count
#2. Dictionaries
# A dictionery stores key-values pairs. For example, take a lookup table wjere every piece of data has a name.
# Dictioneries are created with curly braces {}: Contact = {'name': 'Amara', 'phone': '071 234 5678'}. Access value by key: contact['name'].
#Use .get('key') for safe access - It will return a NONE instead of crashing if the key doesn't exist.
#Key Methods: .key() returns all keys; .value() returns all values; .items() returns (key,value) pairs for iteration.
#3. Lists of Dictioneries
# List of Dictioneries is the most powerful data pattern in beginner Python. Ech dictionery represents one record(a contact, a student, a product)
# and the list holds all the records. This is how database query results and API responses are structured.
#JSON responses from web API's are nearly always lists of dictioneries. Iterating over this structure with a for loop lets you
#process every record in a few lines of code.
#4. Tuples: Immutable Lists
# A Tuple is like a list but immutable, once created, it cannot be changed. 
# Tuples are created using parentheses (): coordinates = (26.2, 28.0). We use tuples when the data sholud not change: GPS coordinates, RGB colour values
# days of the week. Attempting to modify a tuple raises a TypeError.

## YOUTUBE VIDEO NOTES 
# In this lesson we will be learning about:
#1. Lists - Allows us to work with a list of values
#2.Tuples - Allow us to work with sequential data
#3. Sets - Are unordered collecttions of values with no duplicates

#Examples
# LIST
# We need a list of courses
# When dealing with lists we use square brackets [] and seperate the values with a comma [,]
#courses = ['History', 'Math', 'Physics', 'ComSci']

#print(courses) - # This returns the whole list of our courses

# If we want to know how many values are in the list we use the .len() fumnction which stands for length
#print(len(courses)) - # Which will then return a total number of 4. Remember, through the indexing method, it assigns a number to 
# each value and then .len() sums the numbers to get a total/a whole number

# We can also access each value individually but lets print out the list first like we did before
#courses = ['History', 'Math', 'Physics', 'ComSci']

#print(courses[3])  # As i have mentioned abouve that indexing assignes a number to each value which makes it easy to access them
# by just printing out the number assigned to each value
# printing(course[3]) returned ComSci as it was assigned a 3rd location
# NOTE: PYTHON starts counting each value from zero[0] and when counting backward it starts with [-1]
# each number is a LOCATION number e.g 'History' is in "LOCATION[0]" 'Math' "LOCATION[1]"
# We can also use negatives like i have mentioned above to retrieve the last course but using:
# print(courses[-1]), ComSci will be returned again
# So adding to the list changes the position of a value meaning if we add 5 more courses the ComSci will no longer be the last
#value in the list. However [-1] will always returns the last one, whichever it is.
# You can't index values that are not in the list, it will return an Error

##ACCESSING A RANGE OF VALUES INSTEAD OF ONE
# To achieve this we use numbers with a colon[:] e.g [0:3], this methos is called SLICING
# [0:3] mean access values from location 0 but not including location 3
#courses = ['History', 'Math', 'Physics', 'ComSci']

#print(courses[0:3])
#In this regard History, Math and Physics will be return excluding ComSci cause its in excluded location [3]
# by including a colon[:] we are telling python to end at the location before 3
# Even if we say [:3] the results would still be the same
# If we want to show the physics location we would say [3:] puting a colon after 3 assumes that an value after location 3 must be included
#courses = ['History', 'Math', 'Physics', 'ComSci']

#print(courses[3:])
# ComSci will only be returned asit is in location 3 and no any other value will return cause there's no values added
# However, should we have added more courses after ComSci then they would have been included

##MODIFYING OUR LIST
# If we want to add to our list, we use a method called .append()
# Example: we want to add 'Art' in the list of our courses
#courses = ['History', 'Math', 'Physics', 'ComSci']

#courses.append('Art') # before printing we append a value we want to add first and then print the courses variable

#print(courses)
# Returned: ['History', 'Math', 'Physics', 'ComSci', 'Art']

##ADDING A VALUE TO A SPECIFIC LOCATION IN THE LIST
# To achieve this we will instead use the INSERT method 
# INSERT takes two arguments: First it takes the index where you want to insert the value 
# Second: It then takes the value itself
# Example: Putting the course 'ART' in the [0] position/location in the list which is before 'Histtory' 
#courses = ['History', 'Math', 'Physics', 'ComSci']

#courses.insert(0,'Art') # so zero [0] will be our first argument and the 'Art' will be our second argument which is the value itself

#print(courses)
# Returned: ['Art', 'History', 'Math', 'Physics', 'ComSci'] Art is now in location Zero[0]

##USING THE EXTEND METHOD
# We want to use the EXTEND method to add multiple values to the list
#Example
#courses = ['History', 'Math', 'Physics', 'ComSci']
#courses_2 = ['Art', 'Education'] # we want to add these to the main list

#courses.insert(0,courses_2) # Instead of inserting the value 'Art' only like before we will instead add the variable courses_2 

#print(courses)
# Returned: [['Art', 'Education'], 'History', 'Math', 'Physics', 'ComSci'] - so this is a list witin a list
# Its a list withing a list caise ['Art', 'Education'] have squre bruckets which both will be in location 0 
#print(courses[0])
# Returned: ['Art', 'Education'] 
# So this is not the outcome we were looking for as we want the values to each hold a seperate location
# To fix this we will then go back to using the EXTEND method as it only takes one argument which is iterable as its argument
# Pytgon will automatically iterates courses_2 and add each item, one by one, to the main list
# Example
#courses = ['History', 'Math', 'Physics', 'ComSci']
#courses_2 = ['Art', 'Education'] # we want to add these to the main list

#courses.extend(courses_2)
#print(courses)
#Returned: ['History', 'Math', 'Physics', 'ComSci', 'Art', 'Education'] the list is now corrected
# So should we have used append instead of extend, the reslts would have been the same as insert

##REMOVING VALUES FROM THE LIST
#courses = ['History', 'Math', 'Physics', 'ComSci']
#courses.remove('Math') #removes values from the list
#print(courses)
#Returns: ['History', 'Physics', 'ComSci'] 'Math' was removed from the courses list

## ANOTHER WAY OF REMOVING VALUES IS THROUGH THE .POP METHOD
# By default this will remove the last value in the list
# This is useful is we want to use our list as a stacknor CU
#courses = ['History', 'Math', 'Physics', 'ComSci']

#courses.pop() #removes the last value in the list by default

#print(courses)
#Returned: ['History', 'Math', 'Physics'] 'ComSci' was removed 
#NOTE: .pop() can also return the value it removed
#Example
#courses = ['History', 'Math', 'Physics', 'ComSci']

#popped = courses.pop() #grabs the value that was removed
#print(popped)
#print(courses)
#Returned: ComSci
#['History', 'Math', 'Physics']
#If i had a stack or a queue i can keep on popping off values until the list is empty

##SORTING THE LIST
# We now want to reverse the order of the values in the list
# To achive this we will use the .reverse() method
#courses = ['History', 'Math', 'Physics', 'ComSci']

#courses.reverse() #reverses the list

#print(courses)
#Returned: ['ComSci', 'Physics', 'Math', 'History'] our list but in reverse order

#Instead of reversing our list we now ant to sort it
#courses = ['History', 'Math', 'Physics', 'ComSci']

#courses.sort() #sorts the list

#print(courses)
#Returned: ['ComSci', 'History', 'Math', 'Physics'] our list is now sorted in an alphabetical order
#NOTE: if our list had numbers, it word have sorted the in an ASCENDING order (from small to biggest)
#Example
#nums = [1, 5, 2, 4, 3]

#nums.sort() #sorts the list

#print(nums)
#Returned: [1, 2, 3, 4, 5] it sorted the numbers in an ascending order

# Now we want to sort in a descending order
# To achieve thiss we have to pass an argument to our .sort() method called reverse
#nums = [1, 5, 2, 4, 3]

#nums.sort(reverse = True) #sorts the list

#print(nums)
#Returned:  [5, 4, 3, 2, 1] numbers are in a descending order
# NOTE: it is important to note that we dont need to reset the variables when we call most of these methods
# It is just altering the list in place
# But there's another way we can get the sorted version of the list without latering the original list
# So what if we wanted the sorted versionof our list without altering the original one
# We use the sorted function, instead of calling the sort method on our list
# We will instead use the sorted function
# We will pass courses into there now 
#courses = ['History', 'Math', 'Physics', 'ComSci']

#sorted(courses) # passing courses into sorted function

#print(courses)
# Returned: ['History', 'Math', 'Physics', 'ComSci'] the same list as the original list
# Reason being,the sorted funtion doesn't sort the list in place it returns a sorted version of the list
# So to get that sorted list, we have to make a new variable, and set it to the return value of the sorted function
# Example 
#courses = ['History', 'Math', 'Physics', 'ComSci']

#sorted_courses = sorted(courses) # made a new variable, and set it to the return value of the sorted function

#print(sorted_courses)
#Returned: ['ComSci', 'History', 'Math', 'Physics'] now our list is sorted without altering the original list
# sorted courses is now equal to the sorted version of the courses list 
# This is useful for when you don't want to alter the original list

##AGGREGATION: MIN, MAX, SUM
#nums = [1, 5, 2, 4, 3]

#print(min(nums))
#Returned: 1 which is the minimum value
#nums = [1, 5, 2, 4, 3]

#print(max(nums))
#Returned: 5 which is the maximum number in the list
#nums = [1, 5, 2, 4, 3]

#print(sum(nums))
# Returned: 15, it added all the numbers up in the list

##LOOKING FOR AN INDEX OF A CERTAIN VALUE
# To achieve this we will use the index methos
# We want to find the index of ComSci in our list
#courses = ['History', 'Math', 'Physics', 'ComSci']

#print(courses.index('ComSci'))
# Returned: 3 which is the location of ComSci
# Always make sure you look for values that always exist and are spelled correctly or else it will return an ERROR

##CHECKING IF A VALUE IS IN OUR LIST
# To achieve this we will use the IN operator
# Example: Checking whether or not ART is in our list
#courses = ['History', 'Math', 'Physics', 'ComSci']

#print('Art' in courses)
# Returned: FALSE cause no condition was met
# And if we then look for Math
#courses = ['History', 'Math', 'Physics', 'ComSci']

#print('Math' in courses)
# Returned: TRUE, meaning a condition was met

##LOOPING THROUGH VALUES
# To achieve this we will use the loop function
# Basically, we want to crete a loop where looping through each value in gthe list and each loop through item variable will be equal
# to the next item in the list so that's why print(item) line is indented.
# It tells us that the code is executed from within the for loop
#Example
courses = ['History', 'Math', 'Physics', 'ComSci']

for item in courses: 
  print(item) #Indented line: tells us that the code is executed from within the for loop