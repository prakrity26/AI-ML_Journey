import pandas as pd

# Load Titanic Dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Display the first 5 rows
print("Titanic Dataset:")
print(df.head())

# 1. Percentage of Passengers Survived

survival_percentage = df["Survived"].mean() * 100

print("\n1. Survival Percentage:")
print(f"{survival_percentage:.2f}%")


# 2. Survival Rate by Gender

gender_survival = df.groupby("Sex")["Survived"].mean() * 100

print("\n2. Survival Rate by Gender:")
print(gender_survival)


# 3. Average Age of Survivors vs Non-Survivors

average_age = df.groupby("Survived")["Age"].mean()

print("\n3. Average Age:")
print("0 = Did Not Survive")
print("1 = Survived")
print(average_age)


# 4. Passenger Class with Worst Survival Rate

class_survival = df.groupby("Pclass")["Survived"].mean() * 100

print("\n4. Survival Rate by Passenger Class:")
print(class_survival)

worst_class = class_survival.idxmin()

print(f"\nPassenger Class with Worst Survival Rate: {worst_class}")


# 5. Missing Values in Age Column

missing_age = df["Age"].isnull().sum()

print("\n5. Missing Values in Age Column:")
print(missing_age)

# Fill missing Age values with the average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nMissing Age Values After Filling:")
print(df["Age"].isnull().sum())