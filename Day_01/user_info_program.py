#write a program that: asks the user their name, asks their age, tells them what year they were born, and tells them if they are old enough to vote.

print("Enter your name:")
name = input()
print("Enter your age:")
age = input()
age = int(age)

current_year = 2026
year_born = current_year - age

print("\nHello," , name + '!')
print("You were born in:",year_born)

if age>= 18:
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")

