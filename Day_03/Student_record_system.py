# Create a Student class with name, age, and a list of 5 subject marks. Add methods to calculate average, return grade (your logic from Day 2), and save the student's report to a .txt file. Create 3 student objects and save all their reports.

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    # Calculate average marks
    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    # Determine grade
    def get_grade(self):
        average = self.calculate_average()

        if average >= 80:
            return "Distinction"
        elif average >= 40:
            return "Pass"
        else:
            return "Fail"

    # Save report to a text file
    def save_report(self):
        filename = self.name.replace(" ", "_") + "_report.txt"

        with open(filename, "w") as file:
            file.write("------ Student Report ------\n")
            file.write(f"Name: {self.name}\n")
            file.write(f"Age: {self.age}\n")
            file.write(f"Marks: {self.marks}\n")
            file.write(f"Average: {self.calculate_average():.2f}\n")
            file.write(f"Grade: {self.get_grade()}\n")

        print(f"Report saved as {filename}")


# Create 3 student objects
student1 = Student("Ram", 20, [85, 90, 78, 88, 92])
student2 = Student("Shyam", 21, [65, 70, 60, 55, 68])
student3 = Student("Hari", 19, [35, 40, 30, 45, 38])

students = [student1, student2, student3]

# Save reports for all students
for student in students:
    student.save_report()