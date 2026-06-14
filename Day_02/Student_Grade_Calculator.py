# Ask for 5 subject marks, store them in a list, loop through to calculate total and average, write a function that returns "Distinction", "Pass", or "Fail" based on average.
# Function to determine the grade
def calculate_grade(average):
    if average >= 80:
        return "Distinction"
    elif average >= 40:
        return "Pass"
    else:
        return "Fail"

# List to store marks
marks = []

# Input marks for 5 subjects
for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)

# Calculate total using a loop
total = 0
for mark in marks:
    total += mark
average = total / len(marks)

# for result
result = calculate_grade(average)

print("\n----- Student Grade Report -----")
print("Marks:", marks)
print("Total:", total)
print("Average:", average)
print("Result:", result)