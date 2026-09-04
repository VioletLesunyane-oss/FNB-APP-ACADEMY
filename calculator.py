## PYTHON CALCULATOR

# 1. Use float(input()) to collect two numbers from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
# 2. Calculate and display: addition, subtraction, multiplecation, division
sum = int(num1) + int(num2)
sub = int(num1) - int(num2)
mult = int(num1) * int(num2)
div = int(num1) / int(num2)
# 3. Calculate and dispaly: floor division (//) and modulus (%)
floor_div = int(num1) // int(num2)
modu = int(num1) % int(num2)
# 4. Round all results to 2 decimal places using round()
print(round(sum, 2))
print(round(sub, 2))
print(round(mult, 2))
print(round(div, 2))
print(round(floor_div, 2))
print(round(modu, 2))

# 5. Handle division by zero - if the second number is 0, display a friendly error message instead of crashing
if num2 == 0:
    print("Sorry, division by zero cannot be accepted.")
else:
    div = int(num1) / int(num2)
    print(f"Division: {round(div, 2)}")

# 6. Display all results in formatted table using f-string
print(f"Here is the total: {sum}")
print(f"Here is the total: {sub}")
print(f"Here is the total: {mult}")
print(f"Here is the total: {div}")
print(f"Here is the total: {floor_div}")
print(f"Here is the total: {modu}")
