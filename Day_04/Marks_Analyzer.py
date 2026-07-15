# Marks Analyzer with NumPy — Create a NumPy array of 10 students' marks (random numbers 0–100). Calculate and print: mean, max, min, standard deviation. Then create a new array showing which students scored above average (hint: arr[arr > arr.mean()]). Finally, add 5 bonus marks to every student using broadcasting, capping at 100 (hint: use np.clip()).


import numpy as np

# NumPy array of 10 students' marks (random numbers from 0 to 100)
marks = np.random.randint(0, 101, 10)

print("Students' Marks:")
print(marks)

# Calculate and print mean, maximum, minimum, and standard deviation
print("\nMean Marks:", np.mean(marks))
print("Maximum Marks:", np.max(marks))
print("Minimum Marks:", np.min(marks))
print("Standard Deviation:", np.std(marks))

# Students who scored above average
above_average = marks[marks > np.mean(marks)]

print("\nStudents Scoring Above Average:")
print(above_average)

# Add 5 bonus marks to every student (maximum marks = 100)
bonus_marks = np.clip(marks + 5, 0, 100)

print("\nMarks After Adding 5 Bonus Marks:")
print(bonus_marks)