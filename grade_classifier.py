## STUDENT GRADE CLASSIFIER
#1. Collect learner name and marks for three subjects(as float) using input()
learner_name = input("Enter learner's name: ")

math = float(input("Enter math marks: "))
science = float(input("Enter science marks: "))
accounting = float(input("Enter accounting marks: "))


#2. Calculate the average mark accross the three sujects
average_mark = (math + science + accounting) / 3

print(average_mark)

#3. Assign a letter grade:A(80+), B(70-79), C(60-69), D(50-59), F(below 50)

if average_mark >= 80:
    grade = "A"
elif average_mark >= 70:
    grade = "B"
elif average_mark >= 60:
    grade = "C"
elif average_mark >= 50:
    grade = "D"
else:
    grade = "F"

#4. Assign Pass status if the average is 50 or above, fail otherwise
if average_mark >= 50: 
    status = "Pass"
else: 
    status = "Fail"

#5. Flag any individual subject mark below as 'need intervention
if math < 40:
    print("Math: Needs Intervention")
if science < 40:
    print("Science: Needs Intervention")
if accounting < 40:
    print("Accounting: Needs Intervention")

#6. Display a formatted report card showing all inputs, the average mark, the grade, the status and any intervention flag

print("===== STUDENT REPORT CARD =====")
print(f"Learner Name: {learner_name}")
print(f"Math: {math}")
print(f"Science: {science}")
print(f"Accounting: {accounting}")
print(f"Average Mark: {round(average_mark, 2)}")
print(f"Grade: {grade}")
print(f"Status: {status}")












































                