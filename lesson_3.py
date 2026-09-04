## MANIPULATING NUMBERS
# Arithmetic Operations and Type Casting
# Writing a calculator script
# Our code is going to take two inputs from the user, perform some arithmetic operations(add) on them, and display the results.
# Adding two numbers

#num1 = input("Enter the first number: ")
#num2 = input("Enter the second number: ")
#Now we are adding the sum of both numbers and displaying the result in the terminal
#print(num1 + num2)

#Output: 510 returned instead of 15(Basically it combined the numbers instead of summing them together)
#Why: input takes every value as a text and it is stored within a variable as a text, so for an example if we say
# "Hello" + "World" = it will return "HelloWorld"
#So in the terminal i entered the value 5 and the value 10 of which puthon reads it as a text and not numbers
# "5" + "10" = "510". So intead of adding 2 numbers it added 2 string values hence the output of 510

#CORE DATA TYPES
#For one to tackel the issue above, one needs to understand the different data types
#1. str : Strings/Text e.g "Hello". It is a combination of multiple charactors
#2. int: Integer/Whole numbers 5, -1, 10
#3. float : Decimal numbers 5.23, 6.1
#4. bool : True (1) and False (0) Booleans

# Now we investigate what went wrong in the above code
#see below

#TYPE CASTING
#Type casting is moving from one data type to another e.g Convert from int to a str or float of vise versa
#print(int(num1) + int(num2))
#Note: a word "Hello" cannot be converted to an int
#Now our output is 15 cause we converted the str(num1and num2) into an int(5 and 10)

#MATHEMATICAL OPERATORS AND ROUNDING OFF OF FUNCTIONS
#Calculating a tip at the resturant
# The bill is money and with money we always work with decimals so we will use a float
# We gonna take the value of the bill, convert it into a float then store it in the variable "bill"
bill = float(input("Enter the bill: R"))
tip = 0.15 # our 15% is written indecimal
#We then calculate the value of the tip which is the bill * tip
val_tip = bill * tip # In other words its variable 'bill' * variable 'tip'
#We can also calculate the total cost a customer has to pay which is the original bill + value of the tip 
total_cost = bill + val_tip #variable 'bill' + variable val_tip

print(f"Here is the tip: {val_tip}") # Here it will print the total number of bill * tip (val_tip)
print(f"Here is the tip: {round(val_tip, 2)} rounded") # It will then take the total and rounded off into 2 decimal places

print(f"Here is the total cost: {total_cost}") # Here it will print the total of bill + val_tip(total_cost)
print(f"Here is the total coat: {round(total_cost, 2)} rounded") # It will then take the total of total cost and rounded off into 2 decimal places