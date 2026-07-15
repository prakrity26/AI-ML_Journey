
import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

print(df.shape)
print(df.head())
print(df.isnull().sum())       # which columns have missing values?
print(df["Survived"].value_counts())   # how many survived vs died?
print(df.groupby("Sex")["Survived"].mean())  # survival rate by gender
print(df.groupby("Pclass")["Survived"].mean())  # survival by class