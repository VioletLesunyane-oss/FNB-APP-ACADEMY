#Extending the grade classifier into a full grade report generator
# 1. Storing 5 students as a list of dictionaries.
students = [

    {"name": "Mpho", "maths": 95, "english": 67, "science": 89},
    {"name": "Dimpho", "maths": 88, "english": 79, "science": 91},
    {"name": "Lebogang", "maths": 55, "english": 62, "science": 58},
    {"name": "Sarah", "maths": 92, "english": 85, "science": 89},
    {"name": "David", "maths": 45, "english": 51, "science": 48}
]


# 2, 3 and 4. Calculate average, grade, status
# and build the results list
# For my code to make sence and to give it a flow, i will be answering question 2, 3 and 4 in the following sequence:

results = []

for student in students:

    maths = student["maths"]
    english = student["english"]
    science = student["science"]

    # Calculating the average
    average = round((maths + english + science) / 3, 2)

    # Calculating the grade and status
    if average >= 80:
        grade = "A"
        status = "Pass"

    elif average >= 70:
        grade = "B"
        status = "Pass"

    elif average >= 60:
        grade = "C"
        status = "Pass"

    elif average >= 50:
        grade = "D"
        status = "Pass"

    else:
        grade = "F"
        status = "Fail"

    # Creating the result dictionary
    result = {
        "name": student["name"],
        "average": average,
        "grade": grade,
        "status": status
    }

    # Add the result to the results list
    results.append(result)


# 5. Calculating the class average

total_average = 0

for result in results:
    total_average = total_average + result["average"]

class_average = round(total_average / len(results), 2)


# 5.1. Calculating the highest and lowest marks

all_marks = []

for student in students:
    all_marks.append(student["maths"])
    all_marks.append(student["english"])
    all_marks.append(student["science"])

highest_mark = max(all_marks)
lowest_mark = min(all_marks)


# Display the results (OPTIONAL)

print("======GRADE REPORT======")

for result in results:
    print(
        result["name"],
        result["average"],
        result["grade"],
        result["status"]
    )

print()
print("Class average:", class_average)
print("Highest mark:", highest_mark)
print("Lowest mark:", lowest_mark)